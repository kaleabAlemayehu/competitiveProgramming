class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        fs, ft = {}, {}
        for i in range(len(s)):
            fs[s[i]] = fs.get(s[i], 0) + 1 
            ft[t[i]] = ft.get(t[i], 0) + 1 
        for k, v in fs.items():
            if ft.get(k, 0) != v:
                return False
        return True


        