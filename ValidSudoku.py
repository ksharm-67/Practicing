class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        grid = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):

                curr = board[i][j]

                if curr == ".":
                    continue

                grid_index = (i // 3) * 3 + j // 3
                if curr in rows[i] or curr in cols[j] or curr in grid[grid_index]:
                    return False
                
                rows[i].add(curr)
                cols[j].add(curr)
                grid[grid_index].add(curr)

        return True
        