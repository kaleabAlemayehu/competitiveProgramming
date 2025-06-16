class Solution:
    def maxArea(self, height: List[int]) -> int:
        m = 0
        i = 0
        j = len(height) - 1
        while i < j:
            ai = height[i]
            aj = height[j]
            newM = (j - i) * min(ai,aj)
            if newM > m:
                m = newM
            if ai <= aj:
                i += 1
            else:
                j -= 1
        return m
        