class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        
        if n == 0:
            return True
        if m == 0:
            return False
        
        if s[n-1] == t[m-1]:
            return self.isSubsequence(s[:n-1], t[:m-1])
        return self.isSubsequence(s[:n], t[:m-1])
        
       