from fastapi import FastAPI
import os

app = FastAPI()



@app.get("/")
def read_root():
    return {"status":"Backend is running and healthy!"}