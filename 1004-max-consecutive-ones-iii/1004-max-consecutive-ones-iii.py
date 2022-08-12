class Solution:
    def longestOnes(self, s: List[int], k: int) -> int:
        longest, max_repeat, start = 0, 0, 0
        for end in range(len(s)):
            right = s[end]
            if right == 1:
                max_repeat += 1
            
            if (end - start - max_repeat + 1) > k:
                if s[start] == 1:
                    max_repeat -= 1
                start += 1
                
            longest = max(longest, end - start + 1)
        return longest