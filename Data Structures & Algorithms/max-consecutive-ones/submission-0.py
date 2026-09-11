class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        x = 0
        max_consecutive = 0
        for num in nums:
            if num == 1:
                x += 1
                if max_consecutive > x:
                    max_consecutive = max_consecutive
                else:
                    max_consecutive = x
            else:
                x = 0
        return max_consecutive
            



