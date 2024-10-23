class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        inp = len(board)
        # row = [set(x) for x in board]
        row = defaultdict(set)
        col = defaultdict(set)
        square = defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".": continue
                if(board[r][c] in row.get(r,set()) or 
                board[r][c] in col[c] or
                board[r][c] in square[r//3,c//3]): 
                    return False

                col[c].add(board[r][c])
                row[r].add(board[r][c])
                square[r//3,c//3].add(board[r][c])
                print(square)
                print(col)
                # print(square[r//3,c//3])

        return True


