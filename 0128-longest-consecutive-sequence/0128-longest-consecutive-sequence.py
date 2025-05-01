class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)

        count = 0
        max_count = 0

        for n in hashset:
            if n - 1 not in hashset:
                count = 1
                while n + count in hashset:
                    count += 1
                max_count = max(max_count, count)
        return max_count
