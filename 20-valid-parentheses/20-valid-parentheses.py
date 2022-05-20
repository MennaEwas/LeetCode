class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        
        for c in s:
            if c in d.values():
                stack.append(c)
            elif c in d.keys():
                if stack == [] or d[c] != stack.pop():
                    return False
        return stack == []
            