class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        unique = set(nums)
        total_unique = len(unique)

        count = 0
        
        for i in range(len(nums)):
            current_unique = set()
            for j in range(i, len(nums)):
                current_unique.add(nums[j])
                if len(current_unique) == total_unique:
                    count += (len(nums) - j)
                    break
        return count