from pydantic import BaseModel
from typing import List
from subcategory import SubCategory
from substatus import SubStatus
from mongoengine import ReferenceField

class Character(BaseModel):
    id: int
    name: str
    species: ReferenceField(SubCategory)
    status: ReferenceField(SubStatus)
    gender: str

class CharacterCreate(Character):
    pass

class CharacterUpdate(BaseModel):
    name: str
    species: ReferenceField(SubCategory)
    status: ReferenceField(SubStatus)

class CharacterFilter(BaseModel):
    species: ReferenceField(SubCategory) = None
    status: ReferenceField(SubStatus) = None

class CharacterList(BaseModel):
    characters: List[Character]