from pydantic import BaseModel
from typing import List
from character import Character
from episode import Episode
from mongoengine import ReferenceField

class Participation(BaseModel):
    id: int
    character: ReferenceField(Character)
    episode: ReferenceField(Episode)
    start_time: str
    end_time: str
    time: str

class ParticipationCreate(Participation):
    pass

class ParticipationUpdate(BaseModel):
    name: str
    character: ReferenceField(Character)
    episode: ReferenceField(Episode)

class ParticipationFilter(BaseModel):
    character: ReferenceField(Character) = None
    episode: ReferenceField(Episode) = None

class ParticipationList(BaseModel):
    Participations: List[Participation]