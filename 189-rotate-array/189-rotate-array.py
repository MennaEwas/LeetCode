class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        right = nums[:n - k]
        left = nums[n - k:]
        l = left + right
        for i in range(len(nums)):
            nums[i] = l[i]
            
            
            
            
        