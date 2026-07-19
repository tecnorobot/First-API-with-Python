from fastapi import FastAPI
from fastapi.responses import *

app=FastAPI()

@app.get("/")
def serve_home_page() :
    return FileResponse("index.html")
    