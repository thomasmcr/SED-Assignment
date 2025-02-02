from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.database.core import create_db_and_populate_tables, SessionDep
from src.database.schema import Item
from src.api.models import ItemPublic
from sqlmodel import select


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_populate_tables()
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
def home():
    return {"Hello": "World"}

@app.post("/item", response_model=ItemPublic)
def post_item(item: Item, session: SessionDep):
    session.add(item)
    session.commit()
    session.refresh(item)
    return item

@app.get("/items", response_model=list[ItemPublic])
def get_items(session: SessionDep):
    statement = select(Item)
    results = session.exec(statement).all()
    return results 
    
