class Solution:
    def lengthOfLongestSubstring(self, str1: str) -> int:
        d = {}
        startwindow = 0
        longest = 0 

        for i in range(len(str1)):
            right = str1[i]
            if right in d:
                startwindow = max(startwindow, d[right] + 1)
            d[right] = i    
            longest = max(longest, i - startwindow + 1)

        return longest 
