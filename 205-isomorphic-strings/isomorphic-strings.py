class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        pair = {}
        for i, c in enumerate(s):
            if c not in pair:
                if t[i] in pair.values():
                    return False
                pair[c] = t[i]
            else:
                if pair[c] != t[i]:
                    return False
        return True
            
