from apistar import Include, Route
from apistar.handlers import docs_urls, static_urls

from .views import home, welcome

routes = [
    Route('/', 'GET', home),
    Route('/welcome', 'GET', welcome),

    Include('/docs', docs_urls),
    Include('/static', static_urls)
]
