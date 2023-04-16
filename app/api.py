from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from . import crud
from .database import SessionLocal
from app.schemas import (
  TutorCreate,
  TutorGet,
  StudentCreate,
  StudentGet
)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/students/", response_model=StudentGet)
def create_student(
   student: StudentCreate,
   db: Session = Depends(get_db)
   ):
  return crud.create_student(db, student)


@router.get("/students/{student_id}", response_model=StudentGet)
def get_student(student_id: int):
  pass

@router.put("/students/{student_id}", response_model=StudentGet)
def update_student(student_id: int, student: StudentCreate):
  pass

@router.delete("/students/{student_id}")
def delete_student(student_id: int):
  pass

@router.post("/tutor/", response_model=TutorGet)
def create_tutor(tutor: TutorCreate):
    pass

@router.get("/tutor/{tutor_id}", response_model=TutorGet)
def get_tutor(tutor_id: int):
    pass

@router.put("/tutor/{tutor_id}", response_model=TutorGet)
def update_tutor(tutor_id: int, tutor: TutorCreate):
    pass

@router.delete("/tutor/{tutor_id}")
def delete_tutor(tutor_id: int):
    pass
