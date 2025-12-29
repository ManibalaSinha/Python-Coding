def timer(fn):
   def wrapper(*args, **kwargs):
      import time
      start = time.time()
      result = fn(*args, **kwargs)
      print(time.time()-start)
      return result
   return wrapper
@timer
def add(a,b):
   return a+b
print((add(2,4)))
timed_add = timer(add)
#print(timed_add(2,3))
@timer
def process_data(a,b):
    return a*b
#print(process_data(4,5))