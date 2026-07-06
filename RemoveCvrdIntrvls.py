class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        furthest_close = float('-inf')
        intervals.sort(key=lambda x: (x[0], -x[1]))

        for i in intervals:
            if i[1] > furthest_close:
                furthest_close = i[1]
                res += 1
            
            else:
                furthest_close = max(furthest_close, i[1])

        return res 
