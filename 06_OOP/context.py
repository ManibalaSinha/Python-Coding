from contextlib import contextmanager
@contextmanager
def open_file(name):
   f= open(name)
   try: 
      yield f
   finally:
      f.close()
with (open_file("data.csv")) as f:
   print(f.read())