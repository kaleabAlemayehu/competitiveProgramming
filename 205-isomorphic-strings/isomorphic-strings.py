class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ics= defaultdict(list)
        for i, c in enumerate(s):
            ics[c].append(i)
        ict= defaultdict(list)
        for i, c in enumerate(t):
            ict[c].append(i)
        for i, c in enumerate(s):
            if ics[c] != ict[t[i]]:
                return False
        return True

        