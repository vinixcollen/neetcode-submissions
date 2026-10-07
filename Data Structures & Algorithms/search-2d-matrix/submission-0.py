class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for m in range(len(matrix)):
            if target >= matrix[m][0] and target <= matrix[m][len(matrix[m]) - 1]:
                for n in matrix[m]:
                    if target == n:
                        return True
        return False
                
