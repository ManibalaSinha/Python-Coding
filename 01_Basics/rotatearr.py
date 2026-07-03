def rotate_ar(nums,k):
   if not nums:
      return []
   k %= len(nums)
   nums[:] = nums[-k:] + nums[:-k]
   return nums
print(rotate_ar([1,2,3,6,5,4], 3))
