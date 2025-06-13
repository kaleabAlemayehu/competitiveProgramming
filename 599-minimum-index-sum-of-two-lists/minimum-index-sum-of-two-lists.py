class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        res = []
        m = float(inf)
        print(m)
        iMap1 = defaultdict(int)
        for i, v in enumerate(list1):
            iMap1[v] = i
        iMap2 = defaultdict(int)
        for i, v in enumerate(list2):
            if v in iMap1 and i + iMap1[v] <= m:
                if i + iMap1[v] == m:
                    res.append(v)
                    continue
                res = [v]
                m = i + iMap1[v]
        return res
    
        