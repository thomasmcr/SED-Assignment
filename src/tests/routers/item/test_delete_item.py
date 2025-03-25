from fastapi.testclient import TestClient
from sqlmodel import Session
from src.database.schema import Item
from src.tests.utils.item_utils import add_test_item_to_db, get_items_from_db
from src.tests.conftest import app

def test_delete_item_valid(client: TestClient, session: Session):
    test_item: Item = add_test_item_to_db(session=session, name="name", description="description")
    response = client.delete("/item?id=1")
    response_data = response.json()

    assert response.status_code == 200
    assert len(response_data) == len(test_item.__fields__)
    assert response_data["name"] == test_item.name
    assert response_data["description"] == test_item.description
    assert response_data["quantity"] == test_item.quantity

    db_items = get_items_from_db(session=session)
    assert len(db_items) == 0

def test_delete_item_invalid(client: TestClient, session: Session):
    add_test_item_to_db(session=session, name="name", description="description")
    response = client.delete("/item?id=-1")
    response_data = response.json()

    assert response.status_code == 404
    assert len(response_data) == 1
    assert response_data["detail"] == "Item not found"

    db_item = get_items_from_db(session=session)[0]
    assert db_item is not None 
    assert db_item.name == "name"
    assert db_item.description == "description"
    assert db_item.quantity == 1


def test_delete_item_unauthorised(client: TestClient, session: Session):
    app.dependency_overrides.clear()
    add_test_item_to_db(session=session, name="name", description="description")
    response = client.delete("/item?id=0")
    response_data = response.json()

    assert response.status_code == 401
    assert len(response_data) == 1
    assert response_data["detail"] == "Invalid authentication credentials"

    db_item = get_items_from_db(session=session)[0]
    assert db_item is not None 
    assert db_item.name == "name"
    assert db_item.description == "description"
    assert db_item.quantity == 1