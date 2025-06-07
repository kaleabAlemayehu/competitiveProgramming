class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        fq = defaultdict(list)
        for i, n in enumerate(nums):
            fq[n] = fq.get(n, [])
            fq[n].append(i)
        mf =[]
        for key, val  in fq.items():
            if len(val) > len(mf):
                mf = val
            elif len(val)  == len(mf):
                l = len(val) - 1
                if mf[l] - mf[0] > val[l] - val[0]:
                    mf = val
        return  mf[len(mf) - 1] - mf[0] + 1


            


        