class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0 
        for operat in operations:
            if operat[0] == '-' or operat[-1] == '-':
                x -= 1
            else:
                x += 1
        return x