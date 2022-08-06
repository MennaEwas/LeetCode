class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        visited = [0]*n
        minm = []
        for pair in edges:
            visited[pair[1]] = 1
            
        for i in range(n):
            if visited[i] == 0:
                minm.append(i)
                
        return minm
        """
        1. For loop and put the key and list 
        2. make a union between the 2 sets of each until reach the list == n
        3. if the n reached then: return the list of the number of lists 
        4. It is more than 2 
        """
        
        