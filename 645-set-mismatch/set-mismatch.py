class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        fq = Counter(nums)
        missing, duplicated = -1, -1
        for i in range(1, len(nums)+1):
            if fq[i] == 0:
                missing = i 
            elif fq[i] == 2:
                duplicated = i
        return [ duplicated, missing]
                





        