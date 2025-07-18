class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours(k):
            val = 0
            for p in piles:
                val += math.ceil(float(p)/k)

            return val

        l,r=1, max(piles)
        res = r 
        while r >= l:
            m = (r + l) // 2
            if hours(m) <= h:
                res = m
                r = m - 1
            else:
                l = m + 1
        return res
        