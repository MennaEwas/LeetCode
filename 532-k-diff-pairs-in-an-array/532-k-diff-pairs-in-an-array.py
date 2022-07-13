class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        d = {}
        p = 0
        r = []
        #save the unique 
        for i in nums:
            if i not in d.keys():
                d[i] = 1
            else:
                d[i] += 1
                r.append(i)
        if k == 0:
            return len(set(r))
        #check 
        for s in d.keys():
            if (s+k) in d.keys() and (s+k) != s:
                p+=1
        return p
            