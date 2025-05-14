class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hm = {}
        for i, val in enumerate(nums):
            dif = target - val
            if hm.get(dif) != None:
                return [hm.get(dif), i]
            else:
                hm[val] = i
        