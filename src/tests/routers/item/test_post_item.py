from fastapi.testclient import TestClient
from sqlmodel import Session
from src.tests.utils.item_utils import get_items_from_db
from src.tests.conftest import app

def test_post_item_valid(client: TestClient, session: Session):
    response = client.post(
        "/item", 
        json={"name": "name", "description": "description", "quantity": 1}
    )
    response_data = response.json()

    assert response.status_code == 200
    assert len(response_data) == 5
    assert response_data["name"] == "name"
    assert response_data["description"] == "description"
    assert response_data["quantity"] == 1
    assert len(get_items_from_db(session=session)) == 1

def test_post_item_invalid(client: TestClient, session: Session):
    response = client.post(
        "/item", 
        json={"name": "1234", "description": "1234", "quantity": -1}
    )

    assert response.status_code == 422
    assert len(get_items_from_db(session=session)) == 0

def test_post_item_unauthorised(client: TestClient, session: Session):
    app.dependency_overrides.clear()
    response = client.post(
        "/item", 
        json={"name": "name", "description": "description", "quantity": -1}
    )
    response_data = response.json()
    
    assert response.status_code == 401
    assert len(get_items_from_db(session=session)) == 0
    assert len(response_data) == 1
    assert response_data["detail"] == "Invalid authentication credentials"

