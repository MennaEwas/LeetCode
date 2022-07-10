class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums = sorted(nums)
        l = []
        i = 0 
        while i < len(nums):
            if nums[i] == target:
                l.append(i)
            i += 1
        return l