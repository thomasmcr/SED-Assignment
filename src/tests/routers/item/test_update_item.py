from fastapi.testclient import TestClient
from sqlmodel import Session
from src.tests.utils.item_utils import add_test_item_to_db, get_items_from_db
from src.tests.conftest import app

def test_update_item_valid(client: TestClient, session: Session):
    add_test_item_to_db(session=session, name="name", description="description")
    response = client.put(
        "/item", 
        json={"id": 1, "name": "updated name", "description": "updated description", "quantity": 2}
    )
    response_data = response.json()

    assert response.status_code == 200
    assert len(response_data) == 5
    assert response_data["name"] == "updated name"
    assert response_data["description"] == "updated description"
    assert response_data["quantity"] == 2
    assert len(get_items_from_db(session=session)) == 1

    db_item = get_items_from_db(session=session)[0]
    assert db_item is not None 
    assert db_item.name == "updated name"
    assert db_item.description == "updated description"
    assert db_item.quantity == 2

def test_update_item_invalid(client: TestClient, session: Session):
    add_test_item_to_db(session=session, name="name", description="description")
    response = client.put(
        "/item", 
        json={"id": 1, "name": "1234", "description": "1234", "quantity": -1}
    )
    response_data = response.json()

    assert response.status_code == 422
    assert len(response_data) == 1

    db_item = get_items_from_db(session=session)[0]
    assert db_item is not None 
    assert db_item.name == "name"
    assert db_item.description == "description"
    assert db_item.quantity == 1 

def test_update_item_unauthorised(client: TestClient, session: Session):
    app.dependency_overrides.clear()
    add_test_item_to_db(session=session, name="name", description="description")
    response = client.put(
        "/item", 
        json={"id": 1, "name": "updated name", "description": "updated description", "quantity": 2}
    )
    response_data = response.json()

    assert response.status_code == 401
    assert len(response_data) == 1
    assert response_data["detail"] == "Invalid authentication credentials"

    db_item = get_items_from_db(session=session)[0]
    assert db_item is not None 
    assert db_item.name == "name"
    assert db_item.description == "description"
    assert db_item.quantity == 1 
