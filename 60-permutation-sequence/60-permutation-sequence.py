class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        #build permutions with memorization 
        permutations = []
        unused = list(range(1, n+1))
        fact = [1]*(n+1) #base case 
        for i in range(1, n+1):
            fact[i] = i * fact[i-1]
        k -= 1
        while n > 0:
            len_part = fact[n] // n
            i = k//len_part
            permutations.append(unused[i])
            unused.pop(i)
            n -= 1 
            k %= len_part 
        return ''.join(map(str, permutations))
        