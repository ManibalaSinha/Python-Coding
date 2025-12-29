def generate_subsets_iterative(arr):
    result = [[]]  # Start with empty subset
    for num in arr:
        # Add current number to all existing subsets
        result += [curr + [num] for curr in result]
    return result

# Example
arr = [1, 2, 3]
subsets = generate_subsets_iterative(arr)
print("All subsets (iterative):", subsets)
