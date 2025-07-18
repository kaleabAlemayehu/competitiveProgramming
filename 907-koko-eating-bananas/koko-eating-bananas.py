class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1, max(piles)
        res = r 
        while r >= l:
            m = (r + l) // 2
            val = 0
            for i in piles:
                val += math.ceil(float(i)/m)
            if val <= h:
                res = m
                r = m - 1
            else:
                l = m + 1
        return res
        