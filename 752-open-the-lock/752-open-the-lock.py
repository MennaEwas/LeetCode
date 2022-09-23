class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1 
        
        def childern(lock):
            res = []
            for i in range(4):
                #increment
                digit = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
                #decrement
                digit = str((int(lock[i]) - 1 + 10) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
            return res
        
        q = deque()
        visit = set(deadends)
        q.append(["0000", 0]) #lock steps 
        while q:
            lock, steps = q.popleft()
            if lock == target:
                return steps
            for child in childern(lock):
                if child not in visit:
                    visit.add(child)
                    q.append([child, steps+1])
        
        return -1 