from src.dependencies.auth_dependencies import get_current_user_or_throw
from fastapi import APIRouter, Depends, HTTPException, status
from src.database.core import SessionDep
from sqlmodel import col, or_, select
from src.database.schema import Item
from src.models import ItemCreate, ItemPublic, ItemUpdate
import re 

router = APIRouter()

def is_entirely_numeric(test_string):
    return bool(re.fullmatch(r"\d+", test_string))
 
@router.get("/item", response_model=list[ItemPublic], tags=["Item"], dependencies=[Depends(get_current_user_or_throw)])
async def get_items(session: SessionDep, query: str | None):
    if(query):
        statement = select(Item).where(or_(col(Item.name).contains(query), col(Item.description).contains(query)))
    else: 
        statement = select(Item)
    results = session.exec(statement).all()
    return results 

@router.post("/item", response_model=ItemPublic, tags=["Item"], dependencies=[Depends(get_current_user_or_throw)])
def post_item(item: ItemCreate, session: SessionDep):
    new_item = Item(**item.model_dump())
    session.add(new_item)
    session.commit()
    session.refresh(new_item)
    return new_item

@router.put("/item", response_model=ItemPublic, tags=["Item"], dependencies=[Depends(get_current_user_or_throw)])
def put_item(update: ItemUpdate, session: SessionDep):
    if all(value is None for value in [update.name, update.description, update.quantity]):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="All fields cannot be blank"
        )
    
    statement = select(Item).where(Item.id == update.id)
    item_to_update: Item = session.exec(statement).first()
    if(not item_to_update): 
        raise HTTPException(status_code=404, detail=f'Ticket with ID {update.id} not found')

    if(update.name): 
        item_to_update.name = update.name
    if(update.description):
        item_to_update.description = update.description
    if(update.quantity):
        item_to_update.quantity = update.quantity

    session.add(item_to_update)
    session.commit()
    session.refresh(item_to_update)

    return item_to_update


@router.delete("/item", tags=["Item"], dependencies=[Depends(get_current_user_or_throw)])
def delete_item(id: int, session: SessionDep):
    item = session.get(Item, id)
    if not item: 
        raise HTTPException(status_code=404, detail="Item not found")
    session.delete(item)
    session.commit()
    return item

def isBlank(string: str):
    return not(string and string.strip())