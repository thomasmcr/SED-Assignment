from fastapi.testclient import TestClient
from sqlmodel import create_engine, Session, SQLModel
from src.database.core import get_session
from src.main import app
import pytest

TEST_DATABASE_URL = "sqlite:///:memory:"
connect_args = {"check_same_thread": False}
engine = create_engine(TEST_DATABASE_URL, connect_args=connect_args)

#Setup test database
@pytest.fixture(scope="function")
def test_db_session():
    SQLModel.metadata.create_all(engine, checkfirst=True) #Create tables
    session= Session(engine)
    try:
        yield session
    finally:
 
        session.close()

#Setup test app 
@pytest.fixture(scope="module")
def test_client():
    #Overrides the get_session dependency to use the test database session instead
    app.dependency_overrides[get_session] = lambda: test_db_session
    with TestClient(app) as client: 
        yield client
