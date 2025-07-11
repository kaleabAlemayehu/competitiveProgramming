class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i, j = 0, len(s1) - 1
        while j < len(s2):
            count = Counter(s1)
            for p in range(i, j+1):
                if s2[p] in count and count[s2[p]] > 0:
                    count[s2[p]] -= 1
                    if p == j:
                        return True
                    continue
                else:
                    break
            i+=1
            j+=1
        return False