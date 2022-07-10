class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        for i in nums:
            if i == target:
                return True
        return False
        