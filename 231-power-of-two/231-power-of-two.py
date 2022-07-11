class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n > 0:
            return bin(n).count('1') == 1
        else:
            return False
        
            
        