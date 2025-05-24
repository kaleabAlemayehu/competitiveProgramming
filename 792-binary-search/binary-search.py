class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0 
        r = len(nums) - 1
        m = (l + r)//2
        while l <= r:
            if nums[m] < target:
                l = m +1
                m = (l+r)//2
            elif nums[m] > target:
                r = m - 1
                m = (l + r)//2
            else:
                return m
        return -1 

            