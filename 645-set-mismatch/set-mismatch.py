class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        expSum = (n *(n + 1)) / 2
        accSum = sum(nums)
        fq = Counter(nums) 
        for k, v in fq.items():
            if v > 1:
                missed = int(expSum - ( accSum - k))
                return [k, missed]





        