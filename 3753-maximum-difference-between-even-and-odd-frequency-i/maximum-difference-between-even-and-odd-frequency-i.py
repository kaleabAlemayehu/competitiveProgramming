class Solution:
    def maxDifference(self, s: str) -> int:
        fq = Counter(s)
        maxfq, minfq = -1, float(inf) 
        for val in fq.values():
            if val > maxfq and (val % 2) == 1:
                maxfq = val
            elif val < minfq and (val % 2) == 0:
                minfq = val

        return maxfq - minfq
        