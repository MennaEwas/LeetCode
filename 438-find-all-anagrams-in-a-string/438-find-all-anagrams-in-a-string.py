class Solution:
    def findAnagrams(self, str1: str, pattern: str) -> List[int]:
        result_indexes = []
        d = {}
        start, matched = 0, 0
        for p in pattern: 
            if p not in d:
                d[p] = 0
            d[p] += 1

        for end in range(len(str1)):
            right = str1[end]
            if right in d:
                d[right] -= 1
                if d[right] == 0:
                    matched += 1

            if matched == len(d): result_indexes.append(start)

            #Shrinking the window
            if end >= len(pattern) - 1: #need to move 
                left = str1[start]
                start += 1 
                if left in d:
                    if d[left] == 0:
                        matched -= 1
                    d[left] += 1

        return result_indexes