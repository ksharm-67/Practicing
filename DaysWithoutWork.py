class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        
        res, end = 0, meetings[0][1]
        for i in range(1, len(meetings)):
            c = 0
            if meetings[i][0] > end:
                c = meetings[i][0] - end - 1

            end = max(end, meetings[i][1])
            res += c
        
        if meetings[0][0] > 1:
            res += meetings[0][0] - 1
        if end < days:
            res += days - end

        return res
