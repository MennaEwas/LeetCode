class Solution:    
    def checkPowersOfThree(self, n: int) -> bool:
        if n % 3 == 2:
            return False
        elif n > 3:
            n = n // 3
            return self.checkPowersOfThree(n)
        else:
            return True
        