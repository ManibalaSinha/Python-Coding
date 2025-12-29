def find_missing(nums):
   n=len(nums)+1
   total = n*(n+1)//2
   return total - sum(nums)
print(find_missing([1,2,4,5,6]))