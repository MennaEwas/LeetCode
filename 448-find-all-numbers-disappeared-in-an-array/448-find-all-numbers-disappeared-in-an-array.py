class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        a = set(nums)
        l = [i for i in range(1, len(nums)+1)]
        arr = []
        for i in range(len(nums)):
            if l[i] not in a:
                arr.append(l[i])
        return arr
                