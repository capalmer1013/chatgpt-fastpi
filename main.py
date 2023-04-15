from fastapi import FastAPI
from app.api import tutor, student
app = FastAPI()
app.include_router(tutor.router, prefix="/tutors")
app.include_router(student.router, prefix="/students")
