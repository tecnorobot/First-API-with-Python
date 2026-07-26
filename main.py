from fastapi import *
from fastapi.responses import *
from pydantic import BaseModel, Field

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


@app.post("/tasks",status_code=status.HTTP_201_CREATED)
def creatTask(task:Task):
    if not task.title:
        raise HTTPException(status_code=400,detail="Title is empty") 

    #Here I am going to check if database is empty to start with 1 or from new position
    new_id=max(task_DB.keys())+1 if task_DB else 1

    task_DB[new_id]=task.model_dump()

    return {
        "message":"Task successfully created",
        "id":new_id,
        "task":task_DB[new_id]
        }