class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        fq1 = defaultdict(int)
        for i, v in enumerate(list1):
            fq1[v] = i
        fq2 = defaultdict(int)
        for i, v in enumerate(list2):
            if v in fq1:
                fq2[v] = fq1[v] + i
        minimum = min(fq2.values())
        res = []
        for key, val in enumerate(fq2):
            if fq2[val] == minimum:
                res.append(val)
        return res
        