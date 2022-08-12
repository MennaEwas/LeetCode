class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        longest, max_repeat, start = 0, 0, 0
        for end in range(len(s)):
            right = s[end]
            if right not in d:
                d[right] = 0
            d[right] += 1 
            
            max_repeat = max(max_repeat, d[right])
            if (end - start - max_repeat + 1) > k:
                left = s[start]
                d[left] -= 1 
                start += 1
                
            longest = max(longest, end - start + 1)
        return longest