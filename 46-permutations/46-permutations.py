class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        if len(nums)==1:
            return [list(nums)]
        
        for i in range(len(nums)):
            n=nums.pop(0)
            li=self.permute(nums)
            for j in li:
                j.append(n)
            ans.extend(li)
            nums.append(n)
        return ans