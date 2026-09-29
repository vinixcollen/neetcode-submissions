# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        result = []
        ptr = 0
        for i in range(len(pairs)):
            if i == 0:
                result.append(list(pairs))
            else:
                if pairs[i].key < pairs[ptr].key:
                    j = 0
                    while j < i:
                        if pairs[i].key < pairs[j].key:
                            pairs.insert(j, pairs[i])
                            pairs.pop(i + 1)
                        else:
                            j += 1
                    j = 0

                ptr += 1
                result.append(list(pairs))

        return result
