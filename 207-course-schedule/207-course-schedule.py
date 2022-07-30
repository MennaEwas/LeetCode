class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = {i: [] for i in range(numCourses)}
        #fill it 
        for crs, pre in prerequisites:
            premap[crs].append(pre)
        visit = set()
        #dfs 
        def dfs(crs):
            #2 base cases 
            if crs in visit: return False
            if premap[crs] == []: return True
            visit.add(crs)
            
            for pre in premap[crs]:
                if not dfs(pre): return False
                
            visit.remove(crs) #already visited 
            premap[crs] = [] 
            return True
        
        #main function 
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True
        
            
            
            
            
            
        