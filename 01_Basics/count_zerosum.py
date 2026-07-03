def count_zero_sum(nums):
    prefix = 0
    count = 0
    freq = {0: 1}

    for num in nums:
        prefix += num

        if prefix in freq:
            count += freq[prefix]

        freq[prefix] = freq.get(prefix, 0) + 1

    return count
print(count_zero_sum( [1, -1, 2, -2, 3]))
print(count_zero_sum([1,2,3]))
