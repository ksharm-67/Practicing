class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        
        res = []
        for i in range(len(queries)):
            inside = 0
            for j in range(len(points)):
                dist = (queries[i][0] - points[j][0]) ** 2 + (queries[i][1] - points[j][1]) ** 2
                if dist <= queries[i][2] ** 2:
                    inside += 1
            res.append(inside)

        return res
                    
            
