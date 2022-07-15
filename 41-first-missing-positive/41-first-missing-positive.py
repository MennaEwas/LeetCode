class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #find the index of 1 and terminal 
        nums = sorted(nums) #o(nlgn)
        if 1 in nums:
            x = nums.index(1)
            nums = nums[x:]
            i = 0
            n = len(nums)
            
            if n == 2:
                if nums[1] == nums[0] + 1:
                    return nums[1] + 1
                else:
                    return nums[0] + 1
                
            while i < n - 1: 
                if nums[i+1] != (nums[i] + 1) and nums[i] != nums[i+1]:
                    return nums[i] + 1
                i += 1
            return nums[n-1] + 1
            
        else:
            return 1