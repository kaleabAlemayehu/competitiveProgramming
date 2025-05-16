class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res =[1] * len(nums)
        pre = 1
        for i in range(len(nums)):
            res[i] = pre
            pre *= nums[i]
        post = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *=post
            post *= nums[i]
        return res


            

        