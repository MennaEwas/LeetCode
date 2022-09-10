class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def remove(s):
            stack = []
            i = 0 
            while i < len(s):
                if s[i] == '#' and len(stack) > 0:
                    stack.pop() 
                    i += 1
                elif s[i] == '#' and len(stack) == 0:
                    i += 1
                else:
                    stack.append(s[i])
                    i += 1
            return stack

        return remove(s) == remove(t)