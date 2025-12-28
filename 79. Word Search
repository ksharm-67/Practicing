class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        seen, rows, cols = set(), len(board), len(board[0])
        def backtrack(curr, i, j):
            if curr == len(word):
                return True

            if i < 0 or j < 0 or i >= rows or j >= cols or board[i][j] != word[curr] or (i, j) in seen:
                return False

            seen.add((i, j))
            res = (backtrack(curr + 1, i + 1, j) or backtrack(curr + 1, i, j + 1) or backtrack(curr + 1, i - 1, j) or backtrack(curr + 1, i, j - 1))
            seen.remove((i, j))
            return res

        for i in range(rows):
            for j in range(cols):
                if backtrack(0, i, j):
                    return True

        return False        

