class Solution:
    def frequencySort(self, s: str) -> str:
        t = ""
        d = {}
        for c in s: 
            if c not in d.keys():
                d[c] = 1 
            else:
                d[c] += 1 
        
        d = dict(sorted(d.items(), key=lambda item: item[1], reverse = True))
        for k, v in d.items():
            t+= k*v
        
        return t
