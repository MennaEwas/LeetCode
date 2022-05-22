class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(k - 1):
            mx = max(nums)
            nums.remove(mx)
            
        return max(nums)