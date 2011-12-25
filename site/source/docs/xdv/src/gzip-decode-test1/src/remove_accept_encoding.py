
class middleware(object):

    def __init__(self, application):
        self.application = application

    def __call__(self, environ, start_response):
        if 'HTTP_ACCEPT_ENCODING' in environ:
            del environ['HTTP_ACCEPT_ENCODING']
        return self.application(environ, start_response)


def make_middleware(app, global_conf=None):
    return middleware(app)


