class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
                
        #print(d)
        a = 1
        while True:
            v = d.get(a, -1)
            if v == -1: #not here 
                return a
            a+= 1