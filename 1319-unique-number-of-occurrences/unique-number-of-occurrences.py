class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        fq = Counter(arr) 
        return len(fq.values()) == len(set(fq.values()))

    
        

