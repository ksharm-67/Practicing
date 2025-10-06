class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        
        if len(paths) == 1:
            return paths[0][1]

        dest = {}
        for i in range(len(paths)):
            if paths[i][0] not in dest:
                dest[paths[i][0]] = [paths[i][1]]
            else:
                dest[paths[i][0]].append(paths[i][1])

        for key, val in dest.items():
            if val[0] not in dest.keys():
                return val[0]
