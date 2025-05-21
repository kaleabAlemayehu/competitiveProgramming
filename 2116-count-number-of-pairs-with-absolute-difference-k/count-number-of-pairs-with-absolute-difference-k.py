class Solution(object):
    def countKDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        hm = {} 
        for i in range(len(nums)):
            val = hm.get(nums[i], []) 
            val.append(i)
            hm[nums[i]] = val
        res = 0
        for n in nums:
            val1 = n -k
            val2 = n + k
            if hm.get(val1, 0) != 0:
                res += len(hm.get(val1))
            if hm.get(val2, 0) != 0:
                res += len(hm.get(val2))
        return res/2
            
        