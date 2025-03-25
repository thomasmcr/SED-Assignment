from src.database.schema import Item
from sqlmodel import Session, select

def add_test_item_to_db(session: Session, name: str, description: str, quantity: int = 1) -> Item:
    item = Item(name=name, description=description, quantity=quantity)
    session.add(item)
    session.commit()
    session.refresh(item)
    return item 

def get_items_from_db(session: Session) -> list[Item] | None:
    statement = select(Item)
    items = session.exec(statement).all()
    return items 
