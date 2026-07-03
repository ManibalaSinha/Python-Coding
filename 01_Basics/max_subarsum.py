def max_subarray(nums):
    best = nums[0]
    curr = 0

    for num in nums:
        if curr < 0:
            curr = 0
        curr += num
        best = max(best, curr)

    return best
print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))