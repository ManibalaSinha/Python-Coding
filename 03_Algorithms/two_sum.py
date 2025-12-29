def two_sum(nums, target):
   seen = {}
   for i, n in enumerate(nums):
      if target - n in seen:
         return [seen[target-n], i] # return indices
      seen[n] = i
   return []
print(two_sum((1,2,3,4,5,6,7), 9))# return indices