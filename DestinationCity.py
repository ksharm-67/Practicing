class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        
        if len(paths) == 1:
            return paths[0][1]

        dest = {}
        for i in range(len(paths)):
            dest[paths[i][0]] = paths[i][1]

        for val in dest.values():
            if val not in dest:
                return val
