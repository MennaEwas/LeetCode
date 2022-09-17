class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []
        a_ptr, b_ptr = 0, 0
        sa, sb = len(firstList), len(secondList)
        temp = []
        while a_ptr < sa and b_ptr < sb:
            if secondList[b_ptr][0] <= firstList[a_ptr][1] and firstList[a_ptr][0] <= secondList[b_ptr][1]:
                temp.append(max(firstList[a_ptr][0], secondList[b_ptr][0]))
                temp.append(min(firstList[a_ptr][1], secondList[b_ptr][1]))
                res.append(temp)
                temp = []
            if firstList[a_ptr][1] > secondList[b_ptr][1]:
                b_ptr += 1
            else:
                a_ptr += 1
        return res