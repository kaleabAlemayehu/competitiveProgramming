class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        m = 1
        i = 0
        j = 1
        sub = set(s[0])
        while j < len(s):
            if s[j] not in sub:
                sub.add(s[j])
                j+=1
            else:
                i +=1
                j = i + 1
                sub = set(s[i])
            m = max(m, len(sub))
        return m
        