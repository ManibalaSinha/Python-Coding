def findDup(nums):
   seen=set()
   dup=set()
   for n in nums:
      if n in seen:
         return n
      seen.add(n)
   return None
print(findDup([101, 205, 101, 330, 205, 101]))
