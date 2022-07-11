class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        #Negative
        if n < 0:
            return False
        #Base Case
        if n == 1 or n == 4:
            return True
        #Recursive
        elif n > 4:
            n = n / 4
            return self.isPowerOfFour(n)
        else:
            return False
        
#Complixity = lg(n) 
#Space = lg(n)