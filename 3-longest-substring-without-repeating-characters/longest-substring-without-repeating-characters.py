class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = 0
        l = 0
        sub = set()
        for r in range(len(s)):
            while s[r] in sub:
                sub.remove(s[l])
                l+=1
            sub.add(s[r])
            m = max(m, len(sub))
        return m