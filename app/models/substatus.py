from pydantic import BaseModel
from mongoengine import ReferenceField
from status import Status

class SubStatus(BaseModel):
    id: int
    name: str
    category: ReferenceField(Status)

class SubStatusCreate(SubStatus):
    pass