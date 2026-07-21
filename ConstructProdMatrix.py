class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        res = [[1 for i in grid[0]] for j in grid]
        running = 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res[i][j] = running
                running *= grid[i][j]
                running %= 12345
        
        running = 1
        for i in range(len(grid) - 1, -1, -1):
            for j in range(len(grid[0]) - 1, -1, -1):
                res[i][j] *= running
                res[i][j] %= 12345
                running *= grid[i][j] 
                running %= 12345
                    
        return res
