from dotenv import load_dotenv
from typing import Annotated
from fastapi import Depends
from sqlmodel import Session, SQLModel, create_engine
from .schema import * # noqa
import os 

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
connect_args = {"check_same_thread": False}
engine = create_engine(DATABASE_URL, connect_args=connect_args)

def get_session():
    session = Session(engine)
    try: 
        yield session
    finally: 
        session.close()

SessionDep = Annotated[Session, Depends(get_session)]

def create_db_and_populate_tables():
    SQLModel.metadata.create_all(engine, checkfirst=True)

