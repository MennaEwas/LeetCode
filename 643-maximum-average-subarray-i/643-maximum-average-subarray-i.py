class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        arrsum, arrstart = 0, 0
        res = [] 
        for arrend in range(len(nums)):
            arrsum += nums[arrend]
            if arrend >= k-1:
                res.append(arrsum/k)
                arrsum -= nums[arrstart]
                arrstart+=1
        return max(res)