class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        for c in range(2, n - 1):
            sum_count = defaultdict(int)

            for a in range(c):
                for b in range(a + 1, c):
                    sum_count[nums[a] + nums[b]] += 1

            for d in range(c + 1, n):
                target = nums[d] - nums[c]
                count += sum_count.get(target, 0)
                
        return count

                            
