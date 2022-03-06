class Solution:
    
    def __init__(self):
        self.ls = {0: (0, True)}
    def coins(self, c, a):
        if a in self.ls.keys():
            return self.ls[a]
        else:
            ans = []
            for i in range(len(c)):
                if a >= c[i]:
                    k = self.coins(c, a - c[i])
                    f = k[1]
                    if f:
                        ans.append(k[0]+1)
            if len(ans) == 0:
                self.ls[a] = (0, False)
                return (0, False)
            m = min(ans)
            self.ls[a] = (m, True)
            return (m, True)

    def coinChange(self, c: List[int], a: int) -> int:
        k = self.coins(c, a)
        if k[1]:
            return k[0]
        return -1
