class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        minNum = nums[0] 
        maxDiff = -1
        for i in nums:
            maxDiff = max(maxDiff, i - minNum)
            minNum = min(minNum, i)
        return maxDiff if maxDiff != 0 else -1 

            

        