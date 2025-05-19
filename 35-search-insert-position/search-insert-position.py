class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        middle = int((left + right)/ 2) 
        if nums[right] < target:
            return right + 1 
        while left <= right:
            middle = int((left + right)/ 2)
            if nums[middle]  == target:
                return middle
            if nums[middle] < target:
                left = middle+1
                continue
            if nums[middle] > target:
                right = middle-1
                continue
        return left
        