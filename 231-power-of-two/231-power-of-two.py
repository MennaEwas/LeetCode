class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        #Negative
        if n < 0:
            return False
        #Base Case
        if n == 1 or n ==2:
            return True
        #Recursive
        elif n > 2:
            n = n / 2
            return self.isPowerOfTwo(n)
        else:
            return False
        
#Complixity = lg(n) 
#Space = lg(n)
        
            
        