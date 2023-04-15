# app/schemas/tutor.py
from pydantic import BaseModel
class TutorBase(BaseModel):
    name: str
    subject: str
class TutorCreate(TutorBase):
    pass
class Tutor(TutorBase):
    id: int
    class Config:
        orm_mode = True