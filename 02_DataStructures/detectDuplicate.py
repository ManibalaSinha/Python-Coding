def has_duplicates(**nums):
   seen = set()
   for n in nums:
      if n in seen:
         return True
      seen.add(n)
      print(seen)  
   return False
print(has_duplicates(a=1,b=2,c=3,d=4))