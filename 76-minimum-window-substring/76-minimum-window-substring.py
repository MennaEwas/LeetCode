class Solution:
    def minWindow(self, s: str, t: str) -> str:
        start, substr, matched = 0, 0, 0
        d = {}
        min_length = len(s) + 1
        for i in t:
            if i not in d:
                d[i] = 0
            d[i] += 1
            
        for end in range(len(s)):
            right = s[end]
            if right in d:
                d[right] -= 1 
                if d[right] == 0:
                    matched += 1
            while matched == len(d):
                if min_length > end - start + 1:
                    min_length = end - start + 1
                    substr = start
                    
                left = s[start]
                start += 1 
                
                if left in d:
                    if d[left] == 0:
                        matched -= 1 
                    d[left] += 1 
                
        if min_length > len(s):
            return ""
        return s[substr:substr + min_length]
                    
                
            
        