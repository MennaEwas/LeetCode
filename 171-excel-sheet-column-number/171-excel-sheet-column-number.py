class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        n = len(columnTitle)
        sm, pos = 0, 0
        for i in reversed(columnTitle):
            x = ord(i) - 64
            sm += x * 26**pos
            pos+=1
            
        return sm