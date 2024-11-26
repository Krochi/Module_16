from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

user = {'1':'Имя: Name, возраст: 18'}

class User(BaseModel):
    username: str
    age: int

@app.get("/user")
def get_user():
    return user

@app.post("/user{username}/{age}")
def post_user(username: str, age: int):
    user_id = str(max(map(int, user.keys())) + 1)
    user[user_id] = f'Имя:{username}, возраст:{age}'
    return f'User {user_id} is registered'

@app.put("/user{user_id}/{username}/{age}")
def put_user(user_id: int, username: str, age: int):
    if user_id in user:
        user[user_id] = f'Имя: {username}, возраст: {age}'
        return f'User {user_id} has been updated'
    return f'User {user_id} not found'

@app.delete("/user{user_id}")
def delete_user(user_id: int):
    if user_id in user:
        del user[user_id]
        return f'User {user_id} has been deleted'
    return f'User {user_id} not found'
