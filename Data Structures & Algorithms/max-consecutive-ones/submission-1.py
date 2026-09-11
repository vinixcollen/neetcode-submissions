class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        x = 0
        max_count = 0
        for num in nums:
            if num == 1:
                x += 1
                max_count = max(max_count, x)
            else:
                x = 0
        return max_count
            



