import random

class Solution:
    def __init__(self, nums):
        self.nums = nums

    def pick(self):
        res, count = None, 0
        for i, x in enumerate(self.nums, 1):   # i starts at 1
            if random.randint(1, i) == 1:      # pick with prob 1/i
                res = x
        return res
