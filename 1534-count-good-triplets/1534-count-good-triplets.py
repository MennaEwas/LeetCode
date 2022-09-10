class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0 
        def good(t1, t2, result):
            if abs(t1 - t2) <= result:
                return True
            return False
        
        for i in range(len(arr) - 2):
            for j in range(i + 1, len(arr) - 1):
                if good(arr[i], arr[j], a):
                    for k in range(j + 1, len(arr)):
                        if good(arr[j], arr[k], b) and good(arr[k], arr[i], c):
                            count += 1
        
        return count
            