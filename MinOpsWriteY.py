class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        the_rest = defaultdict(int)
        for_y, size = defaultdict(int), len(grid)

        for i in range(size):
            for j in range(len(grid[0])):
                if (i == j or j == size - 1 - i) and i <= size // 2:
                    for_y[grid[i][j]] += 1
                
                elif i > size // 2 and j == size // 2:
                    for_y[grid[i][j]] += 1
                
                else:
                    the_rest[grid[i][j]] += 1
        
        dominating_y, dominating_others = [-1, -1], [-1, -1]
        for k, v in for_y.items():
            if v > dominating_y[1]:
                dominating_y = [k, v]
        for k, v in the_rest.items():
            if v > dominating_others[1]:
                dominating_others = [k, v]

        res = float('inf')

        for y in range(3):
            for other in range(3):
                if y != other:
                    curr = sum(for_y.values()) - for_y[y]
                    curr += sum(the_rest.values()) - the_rest[other]
                    res = min(res, curr)
        
        return res
