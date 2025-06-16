class Solution:
    def maxArea(self, height: List[int]) -> int:
        m = 0
        i = 0
        j = len(height) - 1
        while i < j:
            newM = (j - i) * min(height[i], height[j])
            m = max( newM, m)
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return m
        