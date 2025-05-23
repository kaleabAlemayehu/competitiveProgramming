class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hm = defaultdict()
        for i, n in enumerate(nums):
            if hm.get(n,0) == 0:
                hm[n]= [i]
            else:
                hm[n].append(i)
        for key, fq in hm.items():
            if len(fq) > 1:
                for i in range(len(fq)):
                    for j in range(i+1, len(fq)):
                        if abs(fq[i] - fq[j]) <= k:
                            return True
        return False
            

        
        