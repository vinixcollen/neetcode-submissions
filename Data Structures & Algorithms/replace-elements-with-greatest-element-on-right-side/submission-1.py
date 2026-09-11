class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        p1 = len(arr) - 1
        p2 = len(arr) - 2
        while p2>0:
            if arr[p2] < arr[p1]:
                arr[p2] = arr[p1]
                p2 -= 1
                p1 -= 1
                # print(f"pointer 1: {p1}")
                # print(f"pointer 2: {p2}")
                # print(arr)
            else:
                p2 -= 1
                p1 -= 1
        arr.remove(arr[p2])
        arr.append(-1)
        return arr