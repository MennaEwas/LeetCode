from sortedcontainers import SortedList
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        s = SortedList()
        for i, n in enumerate(nums):
            if i>k: s.remove(nums[i-k-1])
            pos1 = bisect_left(s, n)
            pos2 = bisect_right(s, n)
            if pos1 != pos2: return True
            s.add(n)
        return False
        