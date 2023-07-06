from pydantic import BaseModel
from mongoengine import ReferenceField
from category import Category

class SubCategory(BaseModel):
    id: int
    name: str
    category: ReferenceField(Category)

class SubCategoryCreate(SubCategory):
    pass