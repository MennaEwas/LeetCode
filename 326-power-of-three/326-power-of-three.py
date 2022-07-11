class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 0:
            return False
        if n == 1 or n == 3:
            return True
        
        if n > 3:
            n = n / 3
            return self.isPowerOfThree(n)
        else:
            return False
        