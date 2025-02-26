from typing import Optional
from sqlmodel import Field, SQLModel, Relationship

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    password: str
    is_admin: bool = Field(default=False)

class Item(SQLModel, table=True): 
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: str
    quantity: int
    item_attributes: Optional[list["ItemAttribute"]] = Relationship(back_populates="item")

class ItemAttribute(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    item_id: int = Field(default=None, foreign_key="item.id")
    item: "Item" = Relationship(back_populates="item_attributes")
    attribute_id: int = Field(foreign_key="attribute.id")
    attribute: "Attribute" = Relationship(back_populates="item_attributes")
    value: str
    
class Attribute(SQLModel, table=True): 
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True)
    item_attributes: Optional[list["ItemAttribute"]] = Relationship(back_populates="attribute")