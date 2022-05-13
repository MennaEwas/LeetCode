class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        l = sorted(nums)
        k = []
        for i in l: 
            if i not in k:
                k.append(i)
        if len(k) < 3:
            return k[-1]
        else:
            return k[-3]
        