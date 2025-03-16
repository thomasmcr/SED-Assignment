from src.dependencies.auth_dependencies import get_current_user_or_throw
from fastapi import APIRouter, Depends, HTTPException
from src.database.core import SessionDep
from sqlmodel import col, or_, select
from src.database.schema import Item
from src.models import ItemPublic

router = APIRouter()

@router.get("/item", response_model=list[ItemPublic], tags=["Item"], dependencies=[Depends(get_current_user_or_throw)])
async def get_items(session: SessionDep, query: str | None):
    if(query):
        statement = select(Item).where(or_(col(Item.name).contains(query), col(Item.description).contains(query)))
    else: 
        statement = select(Item)
    results = session.exec(statement).all()
    return results 

@router.post("/item", response_model=ItemPublic, tags=["Item"], dependencies=[Depends(get_current_user_or_throw)])
def post_item(item: Item, session: SessionDep):
    session.add(item)
    session.commit()
    session.refresh(item)
    return item

@router.delete("/item", tags=["Item"], dependencies=[Depends(get_current_user_or_throw)])
def delete_item(id: int, session: SessionDep):
    item = session.get(Item, id)
    if not item: 
        raise HTTPException(status_code=404, detail="Item not found")
    session.delete(item)
    session.commit()
    return { "ok": True, "detail": item}