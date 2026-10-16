class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Recursion practice
        if n == 1:
            return True
        elif n % 2 != 0 or n < 1:
            return False

        n = n // 2
        return self.isPowerOfTwo(n)

    

            
        

        
        