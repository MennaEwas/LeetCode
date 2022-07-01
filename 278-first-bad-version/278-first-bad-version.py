# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        high = n + 1
        low = 1
        while low <= high:
            mid = (low + high) // 2 
            if isBadVersion(mid):
                high = mid - 1
            else:
                low = mid + 1
                mid = low 
        return mid
                
            
        
                
