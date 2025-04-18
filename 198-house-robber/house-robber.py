from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        a, b = 0, 0
        for amount in nums:
            c = max(a, b + amount)
            b = a
            a = c
        return a
