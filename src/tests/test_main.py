from fastapi import Depends
from src.database.core import SessionDep, get_session
from src.database.schema import Item, User
from sqlmodel import Session, select

def test_read_main(client, session: Session):

    user = User(username="test", password="test", is_admin=0)
    session.add(user)
    session.commit()
    session.refresh(user)

    statement = select(User)
    user: User = session.exec(statement).first()
    assert user is not None
    assert user.username == "test"
    assert user.password == "test"

    response = client.get("/")
    assert response.status_code == 200

def test_read_main_two(client, session: Session):
    statement = select(User)
    user: User = session.exec(statement).first()
    assert user is None

def test_get_item(client, session: Session):
    item: Item = Item(id=0, name="test", description="test", quantity=1)
    session.add(item)
    session.commit()
    session.refresh(item)
    response = client.get(
        f"/item?query=f{"test"}"
    )
    assert response.status_code == 200

def test_get_item_two(client, session: Session):
    item: Item = Item(id=1, name="test", description="test", quantity=1)
    session.add(item)
    session.commit()
    session.refresh(item)
    response = client.get(
        f"/item?query=f{"test"}"
    )
    assert response.status_code == 200

def test_items_clear(client, session: Session):
    statement = select(Item)
    items = session.exec(statement).all()
    assert len(items) == 0
