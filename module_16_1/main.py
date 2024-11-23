
from fastapi import FastAPI, Query


app = FastAPI()

@app.get("/")
def get_main_page():
    return {"message": "Главная страница"}

@app.get("/user/admin")
def get_admin_page():
    return {"message": "Ds вошли как администратор"}

@app.get("/user/{user_id}")
def get_user_page(user_id: int):
    return {"message": f"Вы вошли как пользователь № {user_id}"}

@app.get("/user")
def get_user_info(username: str = Query(...), age: int = Query(...)):
    return {"mesaage": f"Информация о пользователе. Имя: {username}, возраст: {age}"}