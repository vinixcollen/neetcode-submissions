from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        # Calculate the distance for each points
        for i in range(len(points)):
            op = math.sqrt((0 - points[i][0])**2 + (0 - points[i][1])**2)
            res.append(op)
        
        # Partition to find pivot
        def partition(res, lo, hi):
            i = lo-1
            j = lo
            pivot = res[hi]

            for j in range(lo, hi):
                if res[j] <= pivot:
                    i += 1
                    res[i], res[j] = res[j], res[i]
                    points[i], points[j] = points[j], points[i]

            i += 1
            res[i], res[hi] = res[hi], res[i]
            points[i], points[hi] = points[hi], points[i]
            return i

        def quickSort(res, lo, hi):
            if lo >= hi:
                return
            
            pivot_index = partition(res, lo, hi)

            quickSort(res, lo, pivot_index - 1)
            quickSort(res, pivot_index + 1, hi)

        quickSort(res, 0, len(res) - 1)
        
        result = []
        for x in range(k):
            result.append(points[x])

        return result