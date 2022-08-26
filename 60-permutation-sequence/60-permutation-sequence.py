class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        permutations = list(itertools.permutations(range(1, n+1)))
        return ''.join(map(str, permutations[k-1]))
        