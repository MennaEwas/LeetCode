class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        l = []
        #sorting
        intervals.sort(key = lambda x: x[0])
        s, e = intervals[0]
        
        for i in range(1, len(intervals)):
            if s <= intervals[i][0] <= e or s <= intervals[i][1] <= e:
                s, e = [min(s, intervals[i][0]), max(e, intervals[i][1])]
                continue
                
            l.append([s, e])
            s, e = intervals[i]
        l.append([s, e])
        return l