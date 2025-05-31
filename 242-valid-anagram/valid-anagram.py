class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        fs = {}
        ft = {}
        for st in s:
            fs[st] = fs.get(st, 0) + 1 
        for ts in t:
            ft[ts] = ft.get(ts, 0) + 1
        for k, v in fs.items():
            if ft.get(k, 0) != v:
                return False
        for k, v in ft.items():
            if fs.get(k, 0) != v:
                return False
        return True


        