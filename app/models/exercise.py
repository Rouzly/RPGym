from sqlalchemy import Column, Integer, String

from app.db.session import Base


class Exercise(Base):
    __tablename__ = "exercises"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    muscle_group = Column(String, nullable=True)