from typing import Optional
from pydantic import BaseModel, field_validator
from sqlmodel import Field

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

class ItemCreate(BaseModel):
    name: str
    description: str 
    quantity: int = Field(gt=0, description="Quantity must be greater than zero")
    
    @field_validator("name")
    def validate_name(cls, v):
        if str(v).isdigit(): 
            print("test")
            raise ValueError("Name cannot be entirely numeric")
        return v 
    
    @field_validator("description")
    def validate_description(cls, v):
        if str(v).isdigit(): 
            print("test")
            raise ValueError("Description cannot be entirely numeric")
        return v 
    
class ItemUpdate(BaseModel):
    id: int
    name: Optional[str] = None
    description: Optional[str] = None
    quantity: Optional[int] = Field(default=None, gt=0, description="Quantity must be greater than zero")

    @field_validator("name")
    def validate_name(cls, v):
        if v is not None and str(v).isdigit():
            print("test")
            raise ValueError("Name cannot be entirely numeric")
        return v 

    @field_validator("description")
    def validate_description(cls, v):
        if v is not None and str(v).isdigit():
            print("test")
            raise ValueError("Description cannot be entirely numeric")
        return v