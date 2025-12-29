def gen():
   for i in range(10):
      yield i
for value in gen():
   print(value)
print(list(gen()))
g= gen()
print(next(g))