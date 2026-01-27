class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [[None for _ in range(3)] for _ in range(3)]
        def check(p: str):
            #rows
            for i in board:
                if (i[0] is not None and i[1] is not None and i[2] is not None) and p == i[0] and p == i[1] and p == i[2]:
                    return True
            
            #cols
            for i in range(3):
                if (board[0][i] is not None and board[1][i] is not None and board[2][i] is not None) and board[0][i] == board[1][i] == board[2][i]:
                    return True

            #diagonals
            if ((board[0][0] == p and board[1][1] == p and board[2][2] == p) or (board[2][0] == p and board[1][1] == p and board[0][2] == p)):
                return True

            #nothing
            return False

        for i in range(len(moves)):
            if not board[moves[i][0]][moves[i][1]]:
                if i % 2 == 0:
                    board[moves[i][0]][moves[i][1]] = 'A'
                    if check('A'):
                        return 'A'
                else:
                    board[moves[i][0]][moves[i][1]] = 'B'
                    if check('B'):
                        return 'B'

        for i in board:
            for j in i:
                if not j:
                    return 'Pending'

        return 'Draw'
