from starlette.applications import Starlette
from starlette.routing import Route
from starlette.templating import Jinja2Templates

templates = Jinja2Templates(directory='templates')

async def index(request):
    return templates.TemplateResponse(
        'index.html', {'name': 'World', 'request': request}
    )

app = Starlette(routes=[
    Route('/', index)
])
