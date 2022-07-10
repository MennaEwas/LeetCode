class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix[0]) #cols
        for i in range(len(matrix)): #rows 
            for j in range(m):
                if target == matrix[i][0] or target == matrix[i][m-1]:
                    return True
                elif target < matrix[i][m-1]:
                    if target > matrix[i][0]:
                        if target == matrix[i][j]:
                            return True
        return False
                