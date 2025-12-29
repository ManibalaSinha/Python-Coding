import requests
from concurrent.futures import ThreadPoolExecutor
urls = [
   "https://jsonplaceholder.typicode.com/todos/1",
   "https://jsonplaceholder.typicode.com/todos/2"
]
def fetch(url):
   resp = requests.get(url)
   return resp.json()
with ThreadPoolExecutor(max_workers=5)