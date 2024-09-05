from pydantic import BaseModel, Field

class TaskRequest(BaseModel):
    title: str = Field(min_length=3, max_length=120)
    description: str = Field(min_length=3, max_length=120)

class TaskEditRequest(BaseModel):
    title: str = Field(min_length=3, max_length=120)
    description: str = Field(min_length=3, max_length=120)
    completed: bool

class TaskCompletedRequest(BaseModel):
    completed: bool