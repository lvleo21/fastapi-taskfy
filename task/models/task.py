from sqlalchemy import Column, Integer, String, Boolean
from core.database import Base


class Task(Base):
    __tablename__ = "tasks"
    TITLE_MAX_LENGHT = 15
    DESCRIPTION_MAX_LENGHT = 30

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    title = Column(String(TITLE_MAX_LENGHT), index=True)
    description = Column(String(DESCRIPTION_MAX_LENGHT))
    completed = Column(Boolean, default=False, index=True)
