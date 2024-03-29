import os
import posixpath
import io
import csv

from dateutil.parser import parse as parse_date
from docutils import nodes
from sphinx import addnodes
from sphinx.domains import Domain
from sphinx.environment.adapters import toctree
from sphinx.util import logging

logger = logging.getLogger(__name__)


# ######################
# patch to toctree._resolve_toctree

resolve_toctree_orig = toctree._resolve_toctree


def modify_toctree(env, pagename, doctree):
    """
    1. compact_paragraph ノードの toctree=True を探す
    2. その子要素の compact_paragraph を探す
    3. compact_paragraph 内の reference の直前に日付を入れる

    <compound classes="toctree-wrapper">
        <compact_paragraph toctree="True">
            <bullet_list>
                <list_item classes="toctree-l1">
                    <compact_paragraph classes="toctree-l1">
                        <reference anchorname="" internal="True" refuri="teratail-3rd-anniv/index.html">
                            2017/07/20 #teratail Meetup 集まっtail#7 - 3周年イベントに参加しました
                        </reference>
                    </compact_paragraph>
                </list_item>
            </bullet_list>
        </compact_paragraph>
    </compound>
    """
    def find_toctree(node):
        return isinstance(node, addnodes.compact_paragraph) and node.get('toctree')

    def find_reference(node):
        return isinstance(node, nodes.reference) and node.get('internal')

    blog_domain = env.get_domain('blog')

    for toctree in doctree.traverse(find_toctree, include_self=True):
        for refnode in toctree.traverse(find_reference):
            base, tail = os.path.split(pagename)
            uri = posixpath.normpath('/'.join([base, refnode['refuri']]))
            docname, ext = os.path.splitext(uri)
            date = blog_domain.get_pub_date(docname)
            if date:
                stringdate = date.strftime('%Y/%m/%d')
                date_wrapper = nodes.emphasis(classes=['blog-article-date'])
                date_wrapper += nodes.Text(stringdate, stringdate)
                refnode.parent.insert(refnode.parent.index(refnode), date_wrapper)


def resolve_toctree_patch(
    env, docname: str, builder, toctree, *,
    prune: bool = True, maxdepth: int = 0, titles_only: bool = False,
    collapse: bool = False, includehidden: bool = False,
):
    doctree = resolve_toctree_orig(
        env, docname, builder, toctree,
        prune=prune, maxdepth=maxdepth, titles_only=titles_only,
        collapse=collapse, includehidden=includehidden)

    if doctree:
        # patch
        modify_toctree(env, docname, doctree)

    return doctree

toctree._resolve_toctree = resolve_toctree_patch


class BlogDomain(Domain):
    """Blogで使うドメイン
    """
    name = 'blog'
    label = 'blog'
    initial_data = {'pub_dates': {}}
    data_version = 1

    # working memory
    docnames = []

    def merge_domaindata(self, docnames, otherdata):
        pass

    def resolve_any_xref(self, env, fromdocname, builder, target, node, contnode):
        return []

    def generate(self, docnames=None):
        return []

    def set_docnames(self, docnames):
        self.docnames = docnames[:]

    def set_pub_date(self, docname, pub_date):
        logger.debug('set <- %s, %s', docname, pub_date)
        self.data['pub_dates'][docname] = pub_date

    def get_pub_date(self, docname):
        pub_date = self.data['pub_dates'].get(docname)
        logger.debug('get -> %s, %s', docname, pub_date)
        return pub_date

    def cache_article_dates(self):
        for docname in self.docnames:
            self.cache_article_date(docname)

    def cache_article_date(self, docname):
        """get date meta data from entry

        :param docname: target docname
        :return: None
        """
        if docname not in self.env.metadata:
            return  # not a blog article

        doc_metadata = self.env.metadata[docname]

        if 'date' not in doc_metadata:
            return  # don't index dateless articles

        try:
            pub_date = parse_date(doc_metadata['date'])
            self.set_pub_date(docname, pub_date)
        except ValueError as exc:
            #probably a nonsensical date
            logger.warning('date parse error: %s in %s', str(exc), docname)


# ##################
# tags
def parse_meta_tags(tags):
    """文字列をCSV記法に従って文字列のリストに変換する

    :param str tags: a csv formatted tag string
    :return: list of tag string
    """
    for tags in csv.reader(io.StringIO(tags), skipinitialspace=True):
        return [t.lower() for t in tags]


def convert_tag_string_into_tags(context):
    """docinfoの ``:tags:`` に書かれた文字列をCSV記法に従って文字列のリストに変換する

    :param Dict context: page context
    :return: None
    """
    try:
        meta = context['meta']
        if meta is None:  # blog content ではない
            raise KeyError('meta')
        tags = context['meta']['tags']
    except KeyError:
        pass
    else:
        context['meta']['tags'] = parse_meta_tags(tags)


# ##############
# handlers

def html_page_context(app, pagename, templatename, context, doctree):
    convert_tag_string_into_tags(context)


def env_before_read_docs(app, env, docnames):
    env.get_domain('blog').set_docnames(docnames)


def env_updated(app, env):
    env.get_domain('blog').cache_article_dates()


# ##############
# setup

def setup(app):
    app.connect('env-before-read-docs', env_before_read_docs)
    app.connect('env-updated', env_updated)
    app.connect('html-page-context', html_page_context)
    app.add_domain(BlogDomain)
    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
