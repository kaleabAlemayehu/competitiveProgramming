class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        fq1 = {}
        fq2 = {}
        for s in words1:
            fq1[s] = fq1.get(s, 0) + 1
        for s in words2:
            if fq1.get(s, 0) == 1:
                fq2[s] = fq2.get(s, 0) + 1
        output = 0 
        for key, val in fq1.items():
            if key in fq2 and fq2[key] == 1 and fq1[key] == 1:
                output +=1

        return output


        

        