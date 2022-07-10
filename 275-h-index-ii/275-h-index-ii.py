class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        l, r = 0, n-1
        while l<=r:
            mid = (l+r)//2
            # if the index of paper is smaller than its corresponding citation value, then search space is on the left of mid
            # n-mid is the number of papers from index mid to the last index
            if (n-mid)<=citations[mid]:
                r = mid - 1
            else:
                l = mid + 1
               
        return n-l