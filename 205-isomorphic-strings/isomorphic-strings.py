class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        pair = {}
        for cs, ct in zip(s,t):
            if cs not in pair:
                if ct in pair.values():
                    return False
                pair[cs] = ct
            else:
                if pair[cs] != ct:
                    return False
        return True
            
