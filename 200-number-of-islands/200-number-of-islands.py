class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            visited.add((i, j)) #set of tuples 
            #make for the same row
            if j+1 < m and (i, j+1) not in visited and grid[i][j+1] == '1':
                dfs(i, j+1)
            if i+1 < n and (i+1, j) not in visited and grid[i+1][j] == '1':
                dfs(i+1, j)
            if j > 0 and (i, j-1) not in visited and grid[i][j-1] == '1':
                dfs(i, j-1)
            if i > 0 and (i-1, j) not in visited and grid[i-1][j] == '1':
                dfs(i-1, j)
            
        
        #main function
        n = len(grid)  #rows
        m = len(grid[0]) #cols
        visited = set()
        NoIsland = 0 
        for i in range(n):
            for j in range(m):
                #starting land 
                if grid[i][j] == '1' and (i, j) not in visited:
                    NoIsland += 1
                    visited.add((i, j))
                    dfs(i, j)

        
        return NoIsland 
    
    
    '''
    Pesudo
    NoIslands = 0
    visited = set() #set of tuples 
    for i in range(rows):
        for j in range(col):
            #starting land 
            if g[i][j] == 1 and noted not in visited:
                NoIslands+= 1
                visited.add(g[i][j])
                #traversing the right and bottom 
                while g[i][j]:
                    if g[i][j+1] == 1: visited.add(g[i][j+1])
                    if g[i+1][j] == 1: visited.add(g[i+1][j])   
               
    
    '''