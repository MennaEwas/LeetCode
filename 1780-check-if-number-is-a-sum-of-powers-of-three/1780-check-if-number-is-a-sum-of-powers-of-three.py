class Solution:    
    def checkPowersOfThree(self, n: int) -> bool:
        if n < 0:
            return False
        r = 0
        while(n != 1 and r != 2):
            r = n % 3
            n = n // 3
            
        return r != 2
            
        