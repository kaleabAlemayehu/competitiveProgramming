class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        acc = [] #pair (index, temp)
        for i, t in enumerate(temperatures):
            while acc and acc[-1][1] < t:
                index, temp = acc.pop()
                res[index] = i - index
            acc.append([i,t])
        return res