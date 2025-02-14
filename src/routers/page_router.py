from fastapi import Request, APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

templates = Jinja2Templates(directory="src/templates")
router = APIRouter()

@router.get("/", tags=["Pages"], response_class=HTMLResponse)
async def home(request: Request):
    path = request.url.path
    return templates.TemplateResponse(
        request=request, name="pages/home.html", context={"path": path}
    )

@router.get("/browse", tags=["Pages"], response_class=HTMLResponse)
async def home(request: Request):
    path = request.url.path
    return templates.TemplateResponse(
        request=request, name="pages/browse.html", context={"path": path}
    )