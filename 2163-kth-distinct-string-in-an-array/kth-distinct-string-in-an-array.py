class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        hm = {} 
        for s in arr:
            hm[s] = hm.get(s, 0) + 1
        res = []
        for key, val in hm.items():
            if val == 1:
                res.append(key)
        if k > len(res):
            return ""
        else:
            return res[k-1]

