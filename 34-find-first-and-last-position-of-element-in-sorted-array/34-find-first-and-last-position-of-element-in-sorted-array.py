class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l =[]
        c = 0 
        for i in nums:
            if i == target:
                l.append(c)
            c += 1
        if len(l):
            return [min(l), max(l)] 
        else:
            return [-1, -1]
        