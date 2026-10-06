class Solution:
    def sortColors(self, nums: List[int]) -> None:
        buckets = [[] for _ in range(3)]
        for num in nums:
            if num == 0:
                buckets[0].append(num)
            elif num == 1:
                buckets[1].append(num)
            else:
                buckets[2].append(num)

        nums.clear()

        for bucket in buckets:
            for num in bucket:
                nums.append(num)


        