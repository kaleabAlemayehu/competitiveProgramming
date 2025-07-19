class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1
        while r >= l:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            m = (l + r + 1) // 2
            res = min(res, nums[m])
            if nums[l] < nums[m]:
                l = m + 1
            else:
                r = m - 1
                
        return res
        