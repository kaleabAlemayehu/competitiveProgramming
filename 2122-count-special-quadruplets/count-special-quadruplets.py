class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        # create storage for result and store length
        res = 0
        l = len(nums)

        count = defaultdict(int)
        count[nums[l-1] - nums[l-2]] = 1
        
        for b in range(l - 3, 0, -1):
            for a in range(b - 1, -1, -1):
                res += count[nums[a] + nums[b]]
            # why treat like b == c ?
            # the current value of b is treated like it is next value of c that is why we put the loop down here not up there before looping over a
            for x in range(l - 1, b, -1):
                count[nums[x] - nums[b]] += 1
        
        return res

                            
