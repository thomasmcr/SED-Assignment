from pydantic import BaseModel

class RegisterUserModel(BaseModel):
    username: str
    password: str

class UserPublic(BaseModel):
    id: int 
    username: str

    class Config:
        from_attributes = True
    
    
class AttributePublic(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True

class ItemAttributePublic(BaseModel):
    id: int
    item_id: int
    attribute: AttributePublic
    value: str

    class Config:
        from_attributes = True

class ItemPublic(BaseModel):
    id: int
    name: str
    description: str
    quantity: int
    item_attributes: list[ItemAttributePublic]

    class Config:
        from_attributes = True