from typing import List
from .student import StudentGet

from pydantic import BaseModel
class TutorBase(BaseModel):
    name: str
    subject: str
class TutorCreate(TutorBase):
    pass
class TutorGet(TutorBase):
    id: int
    students: List[StudentGet] = []