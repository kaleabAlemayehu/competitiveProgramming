class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        c = Counter(chars) 
        total = 0
        for w in words:
            for c in w:
                if chars.count(c) < w.count(c):
                    break
            else:
                total += len(w)
        return total
            

                    
            
        
        