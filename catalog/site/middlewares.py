from catalog.models import Product, Category

class AppMiddleware(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        print 'middleware called'
        return self.app(environ, start_response)
