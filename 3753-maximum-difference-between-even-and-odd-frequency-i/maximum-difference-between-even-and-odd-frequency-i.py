class Solution:
    def maxDifference(self, s: str) -> int:
        fq = Counter(s)
        maxfq, minfq = 0, float(inf) 
        for val in fq.values():
            if (val % 2) == 1:
                maxfq = max(maxfq, val)
            else:
                minfq = min(minfq, val)

        return maxfq - minfq
        