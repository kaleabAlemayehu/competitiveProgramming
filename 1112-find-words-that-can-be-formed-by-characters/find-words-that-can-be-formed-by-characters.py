class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        c = Counter(chars) 
        total = 0
        for w in words:
            nc = Counter(w)
            isGood = True
            for key, val in nc.items():
                if key not in c or val > c[key]:
                    isGood = False
                    break
            if isGood:
                total += len(w)
        return total
            

                    
            
        
        