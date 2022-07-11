class Solution:
    def maximum69Number (self, num: int) -> int:
        s = 0
        l = [int(x) for x in str(num)]
        for i in range(len(l)):
            if l[i] == 6:
                l[i] += 3
                break
            else:
                continue
        for k in range(len(l)):
            s += l[k] * 10**(len(l) - k - 1)
            
        return s
               
        