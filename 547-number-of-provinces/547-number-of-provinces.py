class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(a):
            visited.add(a)
            for b in range(len(isConnected)):
                if b not in visited and isConnected[a][b]: 
                    dfs(b)
            
        
        prov = 0 
        visited = set()
        for a in range(len(isConnected)): #row by row
            if a not in visited:
                prov += 1
                dfs(a)
        
        return prov
                    