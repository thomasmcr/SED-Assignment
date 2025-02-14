from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager
from src.database.core import create_db_and_populate_tables
from src.routers import page_router, api_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_populate_tables()
    yield

app = FastAPI()
app.mount("/static", StaticFiles(directory="src/static"), name="static")
app.include_router(page_router.router)
app.include_router(api_router.router)

