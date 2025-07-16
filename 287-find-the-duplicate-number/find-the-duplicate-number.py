class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # floyd's tortoise and hare algo
        s , f = 0, 0
        while s != f or s == 0 or f == 0:
            s = nums[s]
            f = nums[nums[f]]
        ss = 0
        while ss != s:
            ss = nums[ss]
            s = nums[s]
        return s