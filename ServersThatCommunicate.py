class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        col = defaultdict(list)  # this col : has a pc in row x
        row = defaultdict(list) # this row : has a pc in col x

        ROWS, COLUMNS = len(grid), len(grid[0])
        
        for i in range(ROWS):
            for j in range(COLUMNS):
                if grid[i][j] == 1:
                    col[i].append(j)
                    row[j].append(i)
                    
        res = 0
        for i in range(ROWS):
            for j in range(COLUMNS):
                if grid[i][j] == 1 and (len(col[i]) > 1 or len(row[j]) > 1):
                    res += 1

        return res
                    
