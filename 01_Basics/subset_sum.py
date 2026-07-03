def subset_sums(nums):
    result = []

    def backtrack(i, curr_sum):
        if i == len(nums):
            result.append(curr_sum)
            return

        backtrack(i + 1, curr_sum + nums[i])
        backtrack(i + 1, curr_sum)

    backtrack(0, 0)
    return result
print(subset_sums([1, 2]))
print(subset_sums([1,2,3]))
