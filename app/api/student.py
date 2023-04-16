from fastapi import APIRouter
from app.schemas import student as student_schema
from app.models import student as student_model

router = APIRouter()

@router.post("/", response_model=student_schema.Student)
def create_student(student: student_schema.StudentCreate):
  pass

@router.get("/{student_id}", response_model=student_schema.Student)
def get_student(student_id: int):
  pass

@router.put("/{student_id}", response_model=student_schema.Student)
def update_student(student_id: int, student: student_schema.StudentCreate):
  pass

@router.delete("/{student_id}")
def delete_student(student_id: int):
  pass