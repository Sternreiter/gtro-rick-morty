from pydantic import BaseModel
from typing import List
from subcategory import SubCategory
from substatus import SubStatus
from mongoengine import ReferenceField

class Episode(BaseModel):
    id: int
    name: str
    season: ReferenceField(SubCategory)
    status: ReferenceField(SubStatus)
    gender: str

class EpisodeCreate(Episode):
    pass

class EpisodeUpdate(BaseModel):
    name: str
    season: ReferenceField(SubCategory)
    status: ReferenceField(SubStatus)

class EpisodeFilter(BaseModel):
    season: ReferenceField(SubCategory) = None
    status: ReferenceField(SubStatus) = None

class EpisodeList(BaseModel):
    Episodes: List[Episode]