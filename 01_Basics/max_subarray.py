def max_subarray(nums):
   current = best = nums[0]
   for n in nums[1:]:
      current =  max(n, current+n)
      best = max(best,current)
   return best
print(max_subarray([1,2,3,4]))