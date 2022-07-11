class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        #base case 
        if n < 0:
            return False
        if n == 1 or n ==2:
            return True
        elif n > 2:
            n = n / 2
            return self.isPowerOfTwo(n)
        else:
            return False
        
            
        