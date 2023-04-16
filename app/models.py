from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    tutors = relationship("Tutor", back_populates="student")

class Tutor(Base):
    __tablename__ = "tutors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    subject = Column(String, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    student = relationship("Student", back_populates="tutors")

