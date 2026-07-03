def log(func):
   def wrapper(*args,**kwargs):
      print("calling",func.__name__)
      return func(*args,**kwargs)
   return wrapper
@log
def add(a,b): return a + b 
print(add(2,4))