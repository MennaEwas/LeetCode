class Solution:
    def longestPalindrome(self, s: str) -> int:
        #longest palindrome length = number of even repeated + number of the max(odd)
        d = {}
        mx = 0
        sm = 0
        odd = False
        
        if len(s) == 2 and s[0] == s[1]:
            return len(s)
        elif len(s) == 1 or len(s) == 2:
            return 1
        
        for k in s:
            if k not in d:
                d[k] = 1
            else:
                d[k] += 1
            
        for v in d.values():
            if v % 2 == 0:
                sm += v 
            else:
                mx = max(mx, v) #mx = 3 
                sm +=  v - 1
                odd =  True
        if not odd:
            return sm 
        return sm + 1
        