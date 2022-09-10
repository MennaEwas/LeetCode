class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        best_s = 100000
        nums.sort()
        
        for i in range(len(nums)-2):
            left = i + 1 
            right = len(nums) - 1

            while left < right: 
                s = nums[i] + nums[left] + nums[right]
                if s == target: 
                    return s 
                if abs(target - s) < abs(target - best_s):
                    best_s = s 
                if s <= target:
                    left += 1 
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                else:
                    right -= 1 
        return best_s
                    