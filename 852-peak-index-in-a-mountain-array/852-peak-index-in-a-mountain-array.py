class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        mx, mx1 = 0, 0
        i = 0
        while i < len(arr):
            mx = max(arr[:i+1])
            mx1 = max(arr[i:])
            if mx == mx1:
                return i 
            i+= 1
        