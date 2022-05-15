class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        f = max(nums) + 1
        n = len(nums)
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                nums[i] = f
                n -= 1
        nums.sort()
        nums = nums[:n]
                
        return n