class Solution:
    def pacificAtlantic(self, height: List[List[int]]) -> List[List[int]]:
        n = len(height) #rows
        m = len(height[0]) #cols
        pac = set()
        atle = set()

        
        def dfs_helper(i, j, visited, prev):
            try:
                cur = height[i][j]
            except: 
                pass 
            
            
            #check the coordinations 
            if (j < 0)  or  (i < 0) or j == m or i == n or  (cur < prev) or (i, j) in visited:
                return 
                #add the pair to visit
            visited.add((i, j))
            #check neighbor 
            dfs_helper(i,j+1,visited,cur)
            dfs_helper(i,j-1,visited,cur)
            dfs_helper(i+1,j,visited,cur)
            dfs_helper(i-1,j,visited,cur)
                   
            
        #check top and bottom rows
        for c in range(m):
            dfs_helper(0, c, pac, height[0][c])
            dfs_helper(n-1, c, atle, height[n-1][c])
        #check left and right cols
        for r in range(n):
            dfs_helper(r, 0, pac, height[r][0])
            dfs_helper(r, m-1, atle, height[r][m-1])
                
        winner = []
        #announce the winners 
        for row in range(n):
            for col in range(m):
                if (row, col) in pac and (row, col) in atle:
                    winner.append((row, col))
                
        return winner
                
                
            
            
        