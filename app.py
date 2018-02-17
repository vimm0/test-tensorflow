from apistar import Include, Route
from apistar.frameworks.wsgi import WSGIApp as App
from apistar.handlers import docs_urls, static_urls

from apistar.frameworks.wsgi import WSGIApp as App
from apps.sppais import routes
from settings import settings

app = App(routes=routes.routes,
          settings=settings)

if __name__ == '__main__':
    app.main()
