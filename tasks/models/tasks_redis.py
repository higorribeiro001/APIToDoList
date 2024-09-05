import json
import os
from typing import List
from .tasks_model import Tasks
from redis import StrictRedis
from ..routers.tasks_response import TaskResponse

rd = StrictRedis(host=os.environ.get('HOST_REDIS'), port=6379, db=0)

def data_cache(db, method_use='get') -> List[TaskResponse]:
    cache = rd.get('tasks')
    if cache and method_use=='get':
        return json.loads(cache.decode('utf-8'))
    else:
        data = db.query(Tasks).all()
        data_serializer = [task.as_dict() for task in data]
        rd.set('tasks', json.dumps(data_serializer))
        return data_serializer