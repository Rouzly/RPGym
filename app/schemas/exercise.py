from pydantic import BaseModel, ConfigDict


class ExerciseBase(BaseModel):
    name: str
    muscle_group: str | None = None


class ExerciseCreate(ExerciseBase):
    pass


class ExerciseRead(ExerciseBase):
    id: int

    model_config = ConfigDict(from_attributes=True)