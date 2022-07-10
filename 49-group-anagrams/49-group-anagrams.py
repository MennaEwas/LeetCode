class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {} #key and list
        for i in strs:
            s = ''.join(sorted(i))
            if s not in d.keys():
                d[s] = [i]
            else:
                d[s] += [i]
                
        return list(d.values())
                
                
                