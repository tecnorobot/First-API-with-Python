from fastapi import *
from fastapi.responses import *
from pydantic import BaseModel

app=FastAPI()


class Task(BaseModel):
    title : str
    completed : bool=False

task_DB={
    1:{"title ":"Set up Git","completed":False},
    2:{"title ":"Watch a vedio","completed":False},
    3:{"title ":"push the project","completed":True}
}


@app.get("/")
def getTasks() :
    return{
        "name":"Task API",
        "version":"1.0",
        "endpoints":"[/tasks]"
    }

@app.get("/health")
def healthCheck():
    return {"status":"ok"}


@app.get("/tasks")
def getAllTasks():
    return task_DB
   

@app.get("/tasks/{task_id}")
def getTaskById(task_id :int):
    if task_id not in task_DB:
      raise  HTTPException(status_code=404,detail="Task not found")
    

    return task_DB[task_id]
