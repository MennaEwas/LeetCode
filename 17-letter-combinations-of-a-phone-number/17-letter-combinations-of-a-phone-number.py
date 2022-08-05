class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        D = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
            }
        
        if len(digits) == 0:
            return []
        
        def backtrack(index,path):
            
            if len(path) == len(digits):
                ret.append("".join(path))
                return
            
            
            
            letters = D[digits[index]]
            for letter in letters:
                
                path.append(letter)
                
                backtrack(index+1,path)  # returns once a path is fully formed
                
                path.pop()    # we remove last letter since it should be replace by new letter in for loop
                
        ret = []
        path = []        
        backtrack(0, path)
        return ret
            