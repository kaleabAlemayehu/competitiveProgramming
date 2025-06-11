class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        s = re.sub(r"[.,;\'?*!]", " ", paragraph.lower()).split()
        cnt = Counter(s)
        max = 0
        w = ""
        for key, val in cnt.items():
            if max < val and key not in banned:
                print(key, val)
                max = val
                w = key
            else:
                print(key, val)
        
        return w
        
        
        