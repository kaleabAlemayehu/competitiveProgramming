class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        acc = [] #index
        for i, t in enumerate(temperatures):
            while acc and temperatures[acc[-1]] < t:
                index= acc.pop()
                res[index] = i - index
            acc.append(i)
        return res