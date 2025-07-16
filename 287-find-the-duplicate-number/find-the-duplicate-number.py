class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fq = Counter(nums)
        for key, val in fq.items():
            if val > 1:
                return key
        
        