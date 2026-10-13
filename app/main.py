from fastapi import FastAPI

from app.db.session import Base, engine
from app.models import user, exercise  # noqa: F401
from app.routers import exercises

app = FastAPI(
    title="Gym Progression API",
    description="API для трекинга тренировок с рекомендациями весов",
    version="0.1.0",
)

Base.metadata.create_all(bind=engine)

app.include_router(exercises.router)


@app.get("/health")
def health_check():
    return {"status": "ok"}