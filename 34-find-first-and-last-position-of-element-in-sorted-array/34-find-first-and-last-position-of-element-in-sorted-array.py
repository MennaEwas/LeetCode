class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        s = 0
        d = len(nums) - 1 
        while s <= d:
            if target != nums[s]:
                s += 1
            elif target != nums[d]:
                d -=1
            else:
                return [s, d]
        return [-1, -1]
                
        