class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()
        arr = []
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                arr.append(nums[i-1])
        return set(arr)