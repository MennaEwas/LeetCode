class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #using sliding window 
        if len(nums) < 2:
            return 0
        if len(nums) == 2:
            if nums[0] > nums[1]:
                return 0
            else:
                return 1
        i = 1
        while i < len(nums) - 1:
            if nums[i] > nums[i+1] and nums[i] > nums[i-1]:
                return i 
            i+= 1
        return nums.index(max(nums))
        
        