from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from shared.dependencies import get_db
from shared.exceptions import NotFound
from ..models.tasks_model import Tasks
from ..models.tasks_redis import data_cache
from fastapi_pagination import paginate, add_pagination, Page
from .tasks_request import TaskRequest, TaskCompletedRequest, TaskEditRequest
from .tasks_response import TaskResponse

router = APIRouter(prefix='/tasks')

@router.get("", response_model=Page[TaskResponse])
def find_all(db: Session = Depends(get_db)) -> List[TaskResponse]:
    return paginate(data_cache(db))

@router.get("/{task_id}", response_model=TaskResponse)
def find_by_id(task_id: int,
               db: Session = Depends(get_db)) -> List[TaskResponse]:
    return search_cache([t for t in data_cache(db) if t['id'] == task_id])

@router.post("", response_model=TaskResponse, status_code=201)
def create(task: TaskRequest,
           db: Session = Depends(get_db)) -> TaskResponse:
    new_task = Tasks(
        **task.dict()
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    data_cache(db, 'post')

    return new_task

@router.put("/{task_id}", response_model=TaskResponse, status_code=200)
def update(task_id: int,
           task: TaskEditRequest,
           db: Session = Depends(get_db)) -> TaskResponse:
    existing_task: Tasks = search_by_id(task_id, db)

    existing_task.title = task.title
    existing_task.description = task.description
    existing_task.completed = task.completed

    db.add(existing_task)
    db.commit()
    db.refresh(existing_task)
    data_cache(db, 'put')

    return existing_task

@router.patch("/{task_id}", response_model=TaskResponse, status_code=200)
def task_completed(task_id: int,
           task: TaskCompletedRequest,
           db: Session = Depends(get_db)) -> TaskResponse:
    existing_task: Tasks = search_by_id(task_id, db)
    existing_task.completed = task.completed

    db.add(existing_task)
    db.commit()
    db.refresh(existing_task)
    data_cache(db, 'patch')

    return existing_task

@router.delete("/{task_id}", status_code=204)
def delete(task_id: int,
           db: Session = Depends(get_db)) -> None:
    existing_task: Tasks = search_by_id(task_id, db)
    db.delete(existing_task)
    db.commit()
    data_cache(db, 'delete')

add_pagination(router)

def search_by_id(task_id: int, db: Session) -> Tasks:
    existing_task: Tasks = db.query(Tasks).get(task_id)

    if existing_task is None:
        raise NotFound("Task")
    
    return existing_task

def search_cache(data):
    if len(data) == 0:
        raise NotFound("Task")
    
    return data[0]