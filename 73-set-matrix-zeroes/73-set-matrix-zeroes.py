class Solution:    
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        menna = [x[:] for x in matrix]
        n = len(matrix)  # high
        m = len(matrix[0])  # width

        for i in range(n):
            for j in range(m):
                if menna[i][j] == 0:
                    for k in range(n):
                        matrix[k][j] = 0
                    for k in range(m):
                        matrix[i][k] = 0                
        