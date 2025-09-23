from pydantic import BaseModel


class Task(BaseModel):
    id: int
    title: str
    description: str | None


class TaskCreate(BaseModel):
    title: str
    description: str | None


class TaskUpdate(BaseModel): 
    title: str | None
    description: str | None
