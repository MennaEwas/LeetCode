class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            premap[crs].append(pre)
            
        visitset = set()
        def dfs(crs):
            #base case 
            if crs in visitset:
                #it is a loop
                return False
            if premap[crs] == []:
                #no pre
                return True
            visitset.add(crs)
            for pre in premap[crs]:
                if not dfs(pre): return False
            visitset.remove(crs)
            premap[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True    
            
        