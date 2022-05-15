class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        for i in range(0, len(haystack) - n + 1):
            if needle == haystack[i:i+n]:
                return i 
        return -1
            