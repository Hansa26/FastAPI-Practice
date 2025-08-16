from fastapi import FastAPI

app = FastAPI()

@app.get("/add")
def add(a, b):
    return a + b