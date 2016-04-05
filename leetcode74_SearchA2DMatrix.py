class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])
        i, j = 0, m * n
        
        while i < j:
            mid = i + (j - i) / 2
            val = matrix[mid / n][mid % n]
            if val == target:
                return True
            elif val < target:
                i = mid + 1
            else:
                j = mid
        return False
