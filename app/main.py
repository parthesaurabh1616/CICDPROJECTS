from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message":"Welcome to Calculator API"}

@app.get("/add")
def add(a: float, b: float):
    return {"result": a + b}

@app.get("/subtract")
def subtract(a: float, b: float):
    return {"result": a - b}