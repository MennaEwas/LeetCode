class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        prem = 0 
        grid = [[0]*m] + grid + [[0]*m] #add rows of only zeros at top and bottom of grid  
        for i in range(n+2): 
            grid[i] = [0]+grid[i]+[0] 
            
            
        for r in range(1, n+1):
            for c in range(1, m+1):
                if grid[r][c] == 1:
                    #check corners 
                    if not grid[r-1][c]: prem += 1
                    if not grid[r+1][c]: prem += 1
                    if not grid[r][c-1]: prem += 1
                    if not grid[r][c+1]: prem += 1
        return prem
                
                 