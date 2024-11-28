from fastapi import FastAPI, HTTPException
from typing import Annotated
from fastapi.param_functions import Path
app = FastAPI()

users = {"1": "Имя: Example, возраст: 18"}

@app.get("/users")
def get_users():
    return users

@app.post("/user/{username}/{age}")
def add_user(
    username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username")],
    age: Annotated[int, Path(ge=18, le=120, description="Enter age")]
):
    new_user_id = str(max(map(int, users.keys())) + 1)
    users[new_user_id] = f"Имя: {username}, возраст: {age}"
    return {"message": f"User {new_user_id} is registered"}

@app.put("/user/{user_id}/{username}/{age}")
def update_user(
    user_id: Annotated[str, Path(min_length=1, description="Enter user ID")],
    username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username")],
    age: Annotated[int, Path(ge=18, le=120, description="Enter age")]
):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return {"message": f"User {user_id} has been updated"}

@app.delete("/user/{user_id}")
def delete_user(user_id: Annotated[str, Path(min_length=1, description="Enter user ID")]):
    del users[user_id]
    return {"message": f"User {user_id} has been deleted"}






