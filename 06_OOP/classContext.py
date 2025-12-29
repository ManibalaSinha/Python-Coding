class OpenFile:
   def __init__(self,name):
      self.name = name
   def __enter__(self):
      self.f = open(self.name)
      return self.f
   def __exit__(self, exc_type, exc_val, exc_tb):
      self.f.close()
with OpenFile("data.csv") as f:
   print(f.read())
      