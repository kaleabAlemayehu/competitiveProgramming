class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        f1 = Counter(s1.split(" "))
        f2 = Counter(s2.split(" "))
        res = []
        for key, val in f1.items():
            if key not in f2 and val == 1:
                res.append(key)
        for key, val in f2.items():
            if key not in f1 and val == 1 :
                res.append(key)
        return res




        