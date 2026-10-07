class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo, hi = 0, len(matrix) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if target >= matrix[mid][0] and target <= matrix[mid][len(matrix[mid]) - 1]:
                l, r = 0, len(matrix[mid]) - 1
                while l <= r:
                    m = l + (r-l) //2
                    if target == matrix[mid][m]:
                        return True
                    elif target > matrix[mid][m]:
                        l = m + 1
                    else:
                        r = m - 1
                return False        
            elif target < matrix[mid][0]:
                hi = mid - 1
            else:
                lo = mid + 1
        return False
        
