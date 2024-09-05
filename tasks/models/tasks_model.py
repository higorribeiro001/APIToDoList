from sqlalchemy import Column, Integer, String, Boolean
from shared.database import Base

class Tasks(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(120))
    description = Column(String(120))
    completed = Column(Boolean, default=False)

    def as_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed
        }
