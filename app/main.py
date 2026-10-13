from fastapi import FastAPI

app = FastAPI(
    title="Gym Progression API",
    description="API для трекинга тренировок с рекомендациями весов",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    return {"status": "ok"}