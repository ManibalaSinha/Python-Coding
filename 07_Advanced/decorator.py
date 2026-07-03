def my_decorator(func):
   def wrapper():
      print("1st")
      #func()
      print("3rd")
   return wrapper
@my_decorator
def say_hello():
   print("hello")  
say_hello()