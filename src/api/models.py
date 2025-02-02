from pydantic import BaseModel

class AttributePublic(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class ItemAttributePublic(BaseModel):
    id: int
    item_id: int
    attribute: AttributePublic
    value: str

    class Config:
        orm_mode = True

class ItemPublic(BaseModel):
    id: int
    name: str
    description: str
    quantity: int
    item_attributes: list[ItemAttributePublic]

    class Config:
        orm_mode = True