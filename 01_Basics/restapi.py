from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
app = FastAPI()
class User(BaseModel):
    name: str
    email: EmailStr
users = []
@app.post("/users")
def create_user(user: User):
    users.append(user)
    return {"message": "User created"}
@app.get("/users")
def get_users():
    return users
