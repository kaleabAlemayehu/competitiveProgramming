class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        i = 0
        res = 0
        maxF = 0
        for j in range(len(s)):
            count[s[j]] = count.get(s[j], 0) + 1
            maxF = max(maxF, count.get(s[j]))

            while (j - i + 1) - maxF > k:
                count[s[i]] -= 1
                i += 1
            res = max(res, (j - i + 1))
        return res

        