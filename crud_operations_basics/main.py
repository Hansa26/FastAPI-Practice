from fastapi import FastAPI
from pydantic import BaseModel, model_validator

app = FastAPI()

user_db = {
    1: {"name": "Hansa", "age": 29},
    2: {"name": "Guruprasad", "age": 30}
}

class UserValidation(BaseModel):
    name: str
    age: int


# UPDATE Method - update the user
@app.put("/users/{user_id}")
def user_update(user_id: int, user_data: UserValidation):
    if user_id in user_db:
        user_db[user_id] = dict(user_data)
        return {"message": "User updated successfully!", "id": user_id, "user_info": user_db[user_id]}
    return {"Error": "User not found!"}

# DELETE Method - delete a user
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    if user_id in user_db:
        del user_db[user_id]
        return {"message": "User deleted successfully!"}
    return {"Error": "User not found!"}

# GET Method - retrieve all users
@app.get("/users")
def get_users():
    return user_db

# POST Method - create a user
@app.post("/users")
def create_user(user_data: UserValidation):
    new_id = max(user_db.keys()) + 1 if user_db else 1
    user_db[new_id] = dict(user_data)
    return {"Message": "User Added"}

