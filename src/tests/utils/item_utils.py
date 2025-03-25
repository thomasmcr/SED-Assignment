from src.database.schema import Item
from sqlmodel import Session

def add_test_item_to_db(session: Session, name: str, description: str, quantity: int = 1):
    item = Item(name=name, description=description, quantity=quantity)
    session.add(item)
    session.commit()
    session.refresh(item)
    return item 