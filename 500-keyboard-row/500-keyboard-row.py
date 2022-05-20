class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        r1 = "qwertyuiop"
        r2 = "asdfghjkl"
        r3 = "zxcvbnm"
        l = []
        for k in words:
            c1, c2, c3 = 0,0,0 
            i = k.lower()
            for j in i:
                if j in r1:
                    c1 += 1
                elif j in r2:
                    c2 += 1
                elif j in r3:
                    c3 += 1
            if c1 == len(k) or c2 == len(k) or c3 == len(k):
                l.append(k)
        return l