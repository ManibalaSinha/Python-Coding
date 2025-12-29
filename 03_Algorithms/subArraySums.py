def subarraySum(nums, k):
    count, s = 0, 0
    prefix = {0: 1}
    for n in nums:
        s += n
        count += prefix.get(s-k, 0)
        prefix[s] = prefix.get(s, 0) + 1
    return count
print(subarraySum([1,2,3], 3))