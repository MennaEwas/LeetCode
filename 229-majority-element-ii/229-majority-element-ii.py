class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        l = []
        n = len(nums) // 3
        k = set(nums)
        for i in k:
            if nums.count(i) > n:
                l.append(i)
                
        return l
        