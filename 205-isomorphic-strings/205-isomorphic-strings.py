class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        arr1 = {}
        arr2 = {}
        if len(set(s)) != len(set(t)):
            return False
        for i in range(len(s)):
            if s[i] in arr1 and t[i] in arr2:
                if arr1[s[i]] != arr2[t[i]]:
                    return False
            
            arr1[s[i]] = i
            arr2[t[i]] = i 
        return True
