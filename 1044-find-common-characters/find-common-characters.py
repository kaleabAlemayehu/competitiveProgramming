class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        count = Counter(words[0])
        for i in range(1, len(words)):
            new_count = Counter(words[i])
            for c in count:
                count[c] = min(count[c], new_count[c])
        
        res = []
        for c, v in count.items():
            for f in range(v):
                res.append(c)
        return res
