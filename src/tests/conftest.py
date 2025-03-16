import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine
from sqlmodel.pool import StaticPool
from src.database.core import get_session
from src.database.schema import User
from src.dependencies.auth_dependencies import get_current_user_or_throw
from src.main import app

async def override_get_current_user_or_throw():
    return User(id=0, username="test", password="test", is_admin=1)

@pytest.fixture(name="session")
def session_fixture():
    engine = create_engine(
        "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
    )
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session


@pytest.fixture(name="client")
def client_fixture(session: Session):
    def get_session_override():
        return session

    app.dependency_overrides[get_session] = get_session_override
    app.dependency_overrides[get_current_user_or_throw] = override_get_current_user_or_throw

    with TestClient(app) as client:
        yield client 

    app.dependency_overrides.clear()
