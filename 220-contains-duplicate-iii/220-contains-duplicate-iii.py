from sortedcontainers import SortedList 
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if k<0 or t<0:
            return False
        s = SortedList()
        for i, n in enumerate(nums):
            if i > k: s.remove(nums[i-k-1])
            pos1 = bisect_left(s,n - t)
            pos2 = bisect_right(s, n + t)
            if pos1 != pos2: return True
            s.add(n)
        return False
            