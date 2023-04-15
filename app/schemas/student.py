# app/schemas/student.py
from pydantic import BaseModel
class StudentBase(BaseModel):
    name: str
    grade: int
class StudentCreate(StudentBase):
    pass
class Student(StudentBase):
    id: int
    class Config:
        orm_mode = True