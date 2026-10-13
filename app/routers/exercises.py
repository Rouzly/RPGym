from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.exercise import Exercise
from app.schemas.exercise import ExerciseCreate, ExerciseRead

router = APIRouter(prefix="/exercises", tags=["exercises"])


@router.post("", response_model=ExerciseRead, status_code=status.HTTP_201_CREATED)
def create_exercise(payload: ExerciseCreate, db: Session = Depends(get_db)):
    exercise = Exercise(name=payload.name, muscle_group=payload.muscle_group)
    db.add(exercise)
    db.commit()
    db.refresh(exercise)
    return exercise


@router.get("", response_model=list[ExerciseRead])
def list_exercises(db: Session = Depends(get_db)):
    return db.query(Exercise).all()


@router.get("/{exercise_id}", response_model=ExerciseRead)
def get_exercise(exercise_id: int, db: Session = Depends(get_db)):
    exercise = db.query(Exercise).filter(Exercise.id == exercise_id).first()
    if not exercise:
        raise HTTPException(status_code=404, detail="Exercise not found")
    return exercise


@router.delete("/{exercise_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_exercise(exercise_id: int, db: Session = Depends(get_db)):
    exercise = db.query(Exercise).filter(Exercise.id == exercise_id).first()
    if not exercise:
        raise HTTPException(status_code=404, detail="Exercise not found")
    db.delete(exercise)
    db.commit()
    return None