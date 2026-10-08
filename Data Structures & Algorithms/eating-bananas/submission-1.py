class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()

        lo, hi = 1, piles[len(piles) - 1]
        while lo <= hi:
            k = lo + (hi-lo) // 2

            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)

            if hours > h:
                lo = k + 1
            else:
                hi = k - 1
        
        return lo



                