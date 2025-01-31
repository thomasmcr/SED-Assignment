from fastapi import FastAPI
from contextlib import asynccontextmanager
from .database.core import create_db_and_populate_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_populate_tables()
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
def home():
    return {"Hello": "World"}
    
