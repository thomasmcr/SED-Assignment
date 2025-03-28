from fastapi import Request, APIRouter, Query, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from src.database.core import SessionDep
from src.database.schema import Item, User
from sqlmodel import select
from src.dependencies.auth_dependencies import get_current_user, get_current_user_or_redirect

templates = Jinja2Templates(directory="src/templates")
router = APIRouter()

@router.get("/", response_class=HTMLResponse, tags=["Pages"])
async def home(request: Request, user: User = Depends(get_current_user)):
    path = request.url.path
    return templates.TemplateResponse(
        request=request, name="pages/home.html", context={"path": path, "user": user.get_user_public() if user else None}
    )

@router.get("/browse", tags=["Pages"], response_class=HTMLResponse)
async def browse(request: Request, user: User = Depends(get_current_user_or_redirect)):
    path = request.url.path
    return templates.TemplateResponse(
        request=request, name="pages/browse.html", context={"path": path, "user": user.get_user_public() if user else None}
    )

@router.get("/view/{id}", tags=["Pages"], response_class=HTMLResponse)
async def view(request: Request, id: int, session: SessionDep, old_path = Query("old_path"), user = Depends(get_current_user_or_redirect)):
    statement = select(Item).where(Item.id == id)
    item: Item | None = session.exec(statement).first()
    path = request.url.path
    return templates.TemplateResponse(
        request=request, name="pages/view.html", context={"path": path, "old_path": old_path, "user": user.get_user_public() if user else None, "item": item }
    )

@router.get("/add", tags=["Pages"], response_class=HTMLResponse)
async def add(request: Request, user = Depends(get_current_user_or_redirect)):
    path = request.url.path
    return templates.TemplateResponse(
        request=request, name="pages/add.html", context={"path": path, "user": user.get_user_public() if user else None}
    )

@router.get("/unauthorised", tags=["Pages"], response_class=HTMLResponse)
async def unauthorised(request: Request, old_path: str = Query("old_path"), user: User = Depends(get_current_user)):
    return templates.TemplateResponse(
        request=request, name="pages/unauthorised.html", context={"path": old_path, "user": user.get_user_public() if user else None}
    )