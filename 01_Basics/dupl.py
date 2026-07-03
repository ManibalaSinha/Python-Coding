'''[1,2,3,1] -> True
[1,2,3,4] -> False'''
def unique(nums):
   seen = set()
   result = []
   for n in nums:
      seen.add(n)
      result.append(n)
   return result
'''1. I am using set to get unique number 3. time complexity o(n)'''