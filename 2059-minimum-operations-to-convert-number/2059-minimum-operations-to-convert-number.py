class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        q = collections.deque([(start, 0)])
        visited = {start} #it is a set contains start 
        
        while q: 
            x, c = q.popleft()
            c += 1
            for num in nums:
                for newx in (x+num, x-num, x^num):
                    if newx == goal: return c
                    if newx < 0 or 1000 < newx or newx in visited:
                        continue 
                    visited.add(newx)
                    q.append((newx, c))
        return -1