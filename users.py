from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Inicia el server: uvicorn users:app --reload

# Entidad user
class User(BaseModel):
    name: str
    surname: str
    url: str
    age: int

#users = [User()]    

@app.get("/usersjson")
async def usersjson():
    return [{"name": "Pablo", "surname": "Echegaray", "url": "https://moure.dev", "age": 28},
            {"name": "Pablo", "surname": "Dev", "url": "https://moure.com", "age": 29},
            {"name": "Jonathan", "surname": "Echegaray", "url": "https://moure.com.ar", "age": 30}]
    
@app.get("/usersclass")
async def usersclass():
    return User(name="Pablo", surname="Echegaray", url="https://moure.dev", age= 28)    