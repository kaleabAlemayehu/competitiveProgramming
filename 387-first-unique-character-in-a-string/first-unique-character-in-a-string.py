class Solution:
    def firstUniqChar(self, s: str) -> int:
        fq = Counter(s)
        for i, v in enumerate(s):
            if fq.get(v) == 1:
                return i
        return -1
        