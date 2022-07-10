class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        l = 0
        r = n - 1
        
        while l <= r: 
            mid = (l + r) // 2
            if (n - mid) <= citations[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return n - l
        