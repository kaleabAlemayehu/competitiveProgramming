class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        fq = Counter(nums) 
        return max(fq, key = fq.get)

