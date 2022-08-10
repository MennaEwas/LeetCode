class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        k = math.inf
        arrsum, arrstart = 0, 0
        for arrend in range(len(nums)):
            arrsum += nums[arrend]
            while arrsum >= target:
                k = min(k, arrend-arrstart+1)
                arrsum -= nums[arrstart]
                arrstart+=1
        return k if k != math.inf else 0
                    