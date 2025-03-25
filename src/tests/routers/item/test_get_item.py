from fastapi.testclient import TestClient
from src.database.schema import Item
from sqlmodel import Session
from src.tests.utils.item_utils import add_test_item_to_db
from src.tests.conftest import app

def test_get_item_valid(client: TestClient, session: Session):
    test_item: Item = add_test_item_to_db(session=session, name="name", description="description")
    response = client.get("/item?query=name")
    response_data = response.json()

    assert response.status_code == 200
    assert len(response_data) == 1

    returned_item = response_data[0]
    assert returned_item["name"] == test_item.name
    assert returned_item["description"] == test_item.description
    assert returned_item["quantity"] == test_item.quantity

def test_get_item_unauthorised(client: TestClient, session: Session):
    app.dependency_overrides.clear()
    add_test_item_to_db(session=session, name="name", description="description")
    response = client.get("/item?query=name")
    response_data = response.json()

    assert response.status_code == 401
    assert len(response_data) == 1
    assert response_data["detail"] == "Invalid authentication credentials"