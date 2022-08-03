class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        premap = {i: [] for i in range(numCourses)}
        rl = []
        #fill it 
        for crs, pre in prerequisites: #all of this are pairs 
            premap[crs].append(pre)
            
        visit = set()
        #dfs 
        def dfs(crs):
            #2 base cases 
            if crs in visit: return []
            if premap[crs] == []: 
                rl.append(crs)
                return rl
            visit.add(crs)
            
            for pre in premap[crs]:
                if not dfs(pre): return []
                
            visit.remove(crs) #already visited 
            premap[crs] = [] 
            rl.append(crs)

            return rl
        
        #main function 
        for crs in range(numCourses):
            if not dfs(crs): return []
            rl = list(dict.fromkeys(rl))

        return rl