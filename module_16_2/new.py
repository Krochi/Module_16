from fastapi import FastAPI
from pydantic import BaseModel
from typing import Annotated
from fastapi.param_functions import Path

app = FastAPI()

# Валидация для маршрута /user/{user_id}
@app.get("/user/{user_id}")
def get_user(user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID", examples={ "example_1": { "value": 1 }})]):
    return {"message": f"Вы вошли как пользователь № {user_id}"}

# Валидация для маршрута /user/{username}/{age}
@app.get("/user/{username}/{age}")
def get_user_info(
    username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", examples={ "example_1": { "value": "UrbanUser" }})],
    age: Annotated[int, Path(ge=18, le=120, description="Enter age", examples={ "example_1": { "value": 24 }})]
):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}

