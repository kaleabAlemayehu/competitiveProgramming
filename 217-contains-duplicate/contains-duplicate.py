class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        fqc = defaultdict(int) 
        for n in nums:
            fqc[n] += 1 
            if fqc[n] > 1:
                return True

        return False
            
        