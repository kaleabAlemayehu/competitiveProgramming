class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l = 0
        r = (m *n) - 1
        while l <= r:
            mid = (l + r + 1) // 2
            i = mid // n
            j = mid % n
            if matrix[i][j] < target:
                l = mid + 1
            elif matrix[i][j] > target:
                r = mid - 1
            else:
                return True
                
        return False