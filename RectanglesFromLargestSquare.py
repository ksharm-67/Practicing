class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        maxLen = max(
            min(i[0], i[1]) for i in rectangles
        )
        
        cnt = 0
        for i in rectangles:
            if min(i[0], i[1]) >= maxLen:
                cnt += 1

        return cnt
    
