class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        d = {}
        startwindow = 0
        longest = 0 

        for i in range(len(fruits)):
            right = fruits[i]
            if right not in d:
                d[right] = 0
            d[right] += 1

            while len(d) > 2:
                left_char = fruits[startwindow]
                d[left_char] -= 1 
                if d[left_char] == 0:
                    del d[left_char]
                startwindow += 1
            longest = max(longest, i - startwindow + 1)

        return longest 