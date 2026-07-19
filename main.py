from fastapi import FastAPI
from fastapi.responses import *

app=FastAPI()

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

   
    