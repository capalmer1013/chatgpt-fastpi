from typing import List, Any
from pydantic import BaseModel



class TutorBase(BaseModel):
    name: str
    subject: str

class TutorCreate(TutorBase):
    pass

class TutorGet(TutorBase):
    id: int
    students: List[Any] = []

class StudentBase(BaseModel):
    name: str

class StudentCreate(StudentBase):
    pass

class StudentGet(StudentBase):
    id: int
    tutors: List[TutorGet] = []
