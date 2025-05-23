class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hm = defaultdict()
        for i, n in enumerate(nums):
            if n in hm and abs(hm[n] - i) <= k:
                    return True
            hm[n]= i
        return False
            

        
        