# -*- coding: utf-8 -*-

import os
import sys
import tempfile
import shutil

j = lambda *p:os.path.normpath(os.path.join(*p))

def main(compiler_path, linker_path, static_path, static_prefix,
        theme_path, rule_path, content_path, output_path):

    # clean-up
    if os.path.exists(output_path):
        shutil.rmtree(output_path)
    os.mkdir(output_path)


    fd, xslt_path = tempfile.mkstemp('.xsl', 'theme-')
    os.close(fd)

    # create xslt file by compile
    cmd = [compiler_path,
            '-r', rule_path,
            '-t', theme_path,
            '-o', xslt_path,
            '-a', static_prefix,
            '-p']
    cmd = ' '.join(cmd)
    print cmd
    os.system(cmd)

    # copy theme files
    shutil.copytree(static_path, j(output_path, os.path.basename(static_path)))

    # copy content file or apply theme
    for dirpath, dirnames, filenames in os.walk(content_path):
        target_path = dirpath[len(content_path)+1:]

        if not os.path.exists(j(output_path, target_path)):
            os.mkdir(j(output_path, target_path))

        for filename in filenames:
            from_file = j(dirpath, filename)
            to_file = j(output_path, target_path, filename)

            if os.path.splitext(filename)[1] in ('.htm', '.html'):
                # apply theme
                cmd = [linker_path,
                        '--xsl', xslt_path,
                        '-o', to_file,
                        from_file,
                        ]
                cmd = ' '.join(cmd)
                print cmd
                os.system(cmd)

            else:
                # copy only
                print 'copy', from_file, to_file
                shutil.copy(from_file, to_file)


if __name__ == '__main__':
    cwd = '.'
    compiler_path = j(cwd, 'bin/xdvcompiler')
    linker_path = j(cwd, 'bin/xdvrun')
    static_path = j(cwd, 'static')
    static_prefix = 'static'
    theme_path = j(cwd, 'static/theme.html')
    rule_path = j(cwd, 'static/rule.xml')
    content_path = j(cwd, '../../docs/build/html')
    output_path = j(cwd, 'output')
    main(compiler_path, linker_path, static_path, static_prefix,
            theme_path, rule_path, content_path, output_path)

