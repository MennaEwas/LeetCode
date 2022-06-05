class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)//2
        k = set(nums)
        for i in k:
            if nums.count(i) > n:
                return i
        