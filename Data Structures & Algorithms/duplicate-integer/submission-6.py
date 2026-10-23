class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}

        for x in nums:
            if d.get(x) is None:
                d[x] = 1
            else:
                return True

        return False
        
        
