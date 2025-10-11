class Solution:
    def countPoints(self, rings: str) -> int:
        
        rods = {}
        for i in range(0, len(rings) - 1, 2):
            if rings[i + 1] in rods:    
                if rings[i] not in rods[rings[i + 1]]:
                    rods[rings[i + 1]].append(rings[i])
            else:
                rods[rings[i + 1]] = [rings[i]]

        res = 0    
        for val in rods.values():
            if len(val) == 3:
                res += 1
        
        return res
