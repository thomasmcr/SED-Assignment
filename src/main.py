from fastapi import FastAPI, status
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager
from src.database.core import create_db_and_populate_tables
from src.routers import item_router, page_router, auth_router, user_router
from src.handlers.auth_redirect_handler import AuthRedirect
from src.handlers import auth_redirect_handler

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_populate_tables()
    yield

app = FastAPI(lifespan=lifespan)
app.mount("/static", StaticFiles(directory="src/static"), name="static")
app.include_router(page_router.router)
app.include_router(item_router.router)
app.include_router(auth_router.router)
app.include_router(user_router.router)
app.add_exception_handler(AuthRedirect, auth_redirect_handler.handler)