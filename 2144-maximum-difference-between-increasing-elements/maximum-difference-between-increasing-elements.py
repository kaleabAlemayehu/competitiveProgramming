class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        m = -1
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] != nums[i]:
                    m = max(m, nums[j]- nums[i])
        return m
        