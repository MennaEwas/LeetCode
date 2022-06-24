class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        k = 0
        r = sum(nums)
        for i in range(len(nums)):
            r -= nums[i]
            if k == r:
                return i 
            k += nums[i]
           
        return -1