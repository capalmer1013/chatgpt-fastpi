from pydantic import BaseModel
from typing import List
from .tutor import TutorGet
class StudentBase(BaseModel):
    name: str
class StudentCreate(StudentBase):
    pass
class StudentGet(StudentBase):
    id: int
    tutors: List[TutorGet] = []