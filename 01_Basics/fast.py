from fastapi import FastAPI, HTTPException
app = FastAPI()
users={1:"Alice"}
@app.get("/users/{user_id}")
def get_user(user_id: int):
   if user_id not in users:
      raise HTTPException(status_code =404, detail="user not found")
   return users[user_id]
