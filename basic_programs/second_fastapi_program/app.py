from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Calculator(BaseModel):
    a: int
    b: int

@app.get("/profile")
def read_profile(name):
    return {"message": f"Hello {name!r}, Welcome to Second FastAPI Program!, \nLet's introduce a simple calculator"}

def add_numbers(a:int, b:int) -> int:
    return a + b

def sub_numbers(a:int, b:int) -> int:
    return a - b

@app.post("/add")
def add_model(model: Calculator):
    return add_numbers(model.a, model.b)

@app.post("/sub")
def sub_model(model: Calculator):
    return sub_numbers(model.a, model.b)
