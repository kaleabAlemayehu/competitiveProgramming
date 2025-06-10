class Solution:
    def maxDifference(self, s: str) -> int:
        f = Counter(s)
        a1, a2 = 0, float(inf) 
        for v in f.values():
            if (v % 2) == 1:
                a1 = max(a1, v)
            else:
                a2 = min(a2, v)
        return a1 - a2
        