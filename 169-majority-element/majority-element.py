class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        fq = Counter(nums) 
        nover2 = len(nums)/2
        for key, val in fq.items():
            if val > nover2:
                return key

