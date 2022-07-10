class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #using sliding window 
        return nums.index(max(nums))
        
        