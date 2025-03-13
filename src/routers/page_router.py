from fastapi import Request, APIRouter, Query, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from src.database.schema import User
from src.dependencies.auth_dependencies import get_current_user_redirect

templates = Jinja2Templates(directory="src/templates")
router = APIRouter()

@router.get("/", response_class=HTMLResponse, tags=["Pages"])
async def home(request: Request):
    path = request.url.path
    return templates.TemplateResponse(
        request=request, name="pages/home.html", context={"path": path}
    )

@router.get("/browse", tags=["Pages"], response_class=HTMLResponse, dependencies=[Depends(get_current_user_redirect)])
async def browse(request: Request):
    path = request.url.path
    return templates.TemplateResponse(
        request=request, name="pages/browse.html", context={"path": path}
    )

@router.get("/unauthorised", tags=["Pages"], response_class=HTMLResponse)
async def unauthorised(request: Request, old_path: str = Query("old_path")):
    return templates.TemplateResponse(
        request=request, name="pages/unauthorised.html", context={"path": old_path}
    )