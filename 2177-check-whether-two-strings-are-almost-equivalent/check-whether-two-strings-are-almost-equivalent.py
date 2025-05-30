class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        if len(word1)  != len(word2):
            return False
        fq1 = {}
        fq2 = {}
        for s in word1:
            fq1[s] = fq1.get(s, 0) + 1
        for s in word2:
            fq2[s] = fq2.get(s, 0) + 1
        for k, v in fq1.items():
            val =  fq2.get(k, 0) 
            if abs(val - v) > 3:
                return False
        for k, v in fq2.items():
            val =  fq1.get(k, 0) 
            if abs(val - v) > 3:
                return False
        return True
                

