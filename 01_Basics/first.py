from collections import Counter
def first(s):
   count = Counter(s)
   for c in s:
      if count[c] == 1:
         return c      
   return None
print(first("leetcode"))
print(first("aabb"))

