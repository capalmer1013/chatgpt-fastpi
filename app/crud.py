
from fastapi import HTTPException
from sqlalchemy.orm import Session

from . import models, schemas

def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()

def get_students(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Student).offset(skip).limit(limit).all()

def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def update_student(
        db: Session,
        student_id: int,
        student: schemas.StudentCreate
        ):
    db_student = get_student(db, student_id)
    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")
    db_student.name = student.name
    db.commit()
    db.refresh(db_student)
    return db_student

def delete_student(
        db: Session,
        student_id: int
        ):
    db_student = get_student(db, student_id)
    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")
    db.delete(db_student)
    db.commit()
    return db_student

def get_tutor(db: Session, tutor_id: int):
    return db.query(models.Tutor).filter(models.Tutor.id == tutor_id).first()

def get_tutors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Tutor).offset(skip).limit(limit).all()

def create_tutor(
        db: Session,
        tutor: schemas.TutorCreate
        ):
    db_tutor = models.Tutor(**tutor.dict())
    db.add(db_tutor)
    db.commit()
    db.refresh(db_tutor)
    return db_tutor

def update_tutor(
        db: Session,
        tutor_id: int,
        tutor: schemas.TutorCreate
        ):
    db_tutor = get_tutor(db, tutor_id)
    if not db_tutor:
        raise HTTPException(status_code=404, detail="Tutor not found")
    db_tutor.name = tutor.name
    db_tutor.email = tutor.email
    db_tutor.phone = tutor.phone
    db.commit()
    db.refresh(db_tutor)
    return db_tutor

def delete_tutor(
        db: Session,
        tutor_id: int
        ):
    db_tutor = get_tutor(db, tutor_id)
    if not db_tutor:
        raise HTTPException(status_code=404, detail="Tutor not found")
    db.delete(db_tutor)
    db.commit()
    return db_tutor
