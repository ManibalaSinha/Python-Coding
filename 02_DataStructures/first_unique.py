from collections import Counter
def first_unique(s):
   count= Counter(s)
   for c in s:
      if count[c] ==1:
         return c
      
   return None
print(first_unique("abcdane"))