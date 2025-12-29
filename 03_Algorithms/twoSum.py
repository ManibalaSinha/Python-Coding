def pair_sum(nums, target):
   seen =set()
   for num in nums:
      if target-num in seen:
         return (target-num , num)
      seen.add(num)
   return None
print(pair_sum([2,7,11,15], 9))
""" def find_pair(nums, target):
    seen = set()
    for num in nums:
        complement = target - num
        if complement in seen:
            return (complement, num)  # Pair found
        seen.add(num)
    return None  # No pair found

# Example
nums = [2, 7, 11, 15]
target = 9
print(find_pair(nums, target))  # Output: (2, 7)
 """