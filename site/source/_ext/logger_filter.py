import logging
from sphinx.util import logging as sphinx_logging


class FilterAll(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        if record.msg.startswith("Overwriting "):
            return False
        return True


def setup_logger_filter():
    name = 'sphinx_reredirects'
    logger = sphinx_logging.getLogger(name)
    logger.logger.addFilter(FilterAll())


# ##############
# setup

def setup(app):
    setup_logger_filter()
    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
