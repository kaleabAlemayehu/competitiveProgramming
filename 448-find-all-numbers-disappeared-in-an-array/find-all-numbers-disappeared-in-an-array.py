class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s = set(nums)
        res = []
        for i in range(1, len(nums) + 1):
            if not (i in s):
                res.append(i)
        return res

        