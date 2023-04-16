from fastapi import APIRouter
from app.schemas import tutor as tutor_schema
from app.models import tutor as tutor_model
router = APIRouter()
@router.post("/", response_model=tutor_schema.Tutor)
def create_tutor(tutor: tutor_schema.TutorCreate):
    pass
@router.get("/{tutor_id}", response_model=tutor_schema.Tutor)
def get_tutor(tutor_id: int):
    pass
@router.put("/{tutor_id}", response_model=tutor_schema.Tutor)
def update_tutor(tutor_id: int, tutor: tutor_schema.TutorCreate):
    pass
@router.delete("/{tutor_id}")
def delete_tutor(tutor_id: int):
    pass