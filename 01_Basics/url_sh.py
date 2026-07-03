from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
import string
import random
import redis
app = FastAPI()
r = redis.Redis(host = 'localhost', port = 6379, db=0, decode_responses = True)
def generate_short_code(length =6):
   chars= string.ascii_letters + string.digits
   return ''.join(random.choice(chars) for _ in range(length))
@app.post("/shorten")
def 