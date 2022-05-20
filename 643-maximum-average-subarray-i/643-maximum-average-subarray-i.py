class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        summ = sum(nums[0:k])
        av = summ / k
        i = 1
        while i < len(nums)-k + 1:
            summ = summ + nums[k+i-1] - nums[i-1]
            av, i = max(av, summ/k),i+1
        return av