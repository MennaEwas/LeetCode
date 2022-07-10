class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums = sorted(nums)
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return nums[i]