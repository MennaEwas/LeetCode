class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        w = 0 
        s = float('-inf')
        i = 0  
        while i < len(nums):
            w += nums[i]
            s = max(s, w)
            w = max(w, 0)
            
            i += 1 
        return s
            
                
                
        