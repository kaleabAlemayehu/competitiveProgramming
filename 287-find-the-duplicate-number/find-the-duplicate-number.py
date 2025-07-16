class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # floyd's tortoise and hare algo
        s , f = nums[0], nums[nums[0]]
        while s != f:
            s = nums[s]
            f = nums[nums[f]]
        ss = 0
        while ss != s:
            ss = nums[ss]
            s = nums[s]
        return s