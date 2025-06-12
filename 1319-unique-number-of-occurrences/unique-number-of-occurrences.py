class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        fq = Counter(arr) 
        fl = list(fq.values())
        fs = set(fl)
        for v in fs:
            fl.remove(v)
        return len(fl) == 0

    
        

