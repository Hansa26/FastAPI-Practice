from fastapi import FastAPI

app = FastAPI()

@app.get("/profile")
def read_profile(name):
    return {"message": f"Hello {name!r}, Welcome to Second FastAPI Program!"}