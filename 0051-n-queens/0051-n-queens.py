class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        board = [["." for i in range(n)] for j in range(n)]
        res= []
        # res.append(list(["".join(row)] for row in board))
        print(res)
        print(board)
        diagSet, antiDiag =set(),set()
        col = set()
        def backTrack(ro):
            if ro >= n:
                res.append(["".join(row) for row in board])
                return
            
            for c in range(n):
                if c not in col and (ro+c) not in diagSet and (ro-c) not in antiDiag:
                    col.add(c)
                    diagSet.add((ro+c))
                    antiDiag.add((ro-c))
                    board[ro][c] = "Q"
                    backTrack(ro+1)
                    board[ro][c] = "."
                    col.discard(c)
                    diagSet.discard((ro+c))
                    antiDiag.discard((ro-c))
        backTrack(0)
        return res


# 00. 011-1 022-2
# 1011 11 123-1 
# 202-2 2131 2240



#         def backtracking(col, row, diagSet, antiDiag):

#         backtracking(set(), set(), set(), set())
#         if basecase:
#             append res
#             return

#         for c in combinations
#             if valid: 
#                 add
#                 backtrack dfs

#                 pop

#         return res

#                     ""

#         "Q..." ".Q.." "...Q" "..Q."

# "Q..." ".Q.." "..Q." "...Q"























        # posDiag = set() #r+c
        # negDiag = set() #r-c
        # col = set()
        # res = []
        # board = [["."]*n for row in range(n)]
        # def backtracking(ro):
        #     if ro >= n: 
        #         res.append(["".join(rows) for rows in board[:]])
        #         return
        #     for cols in range(n):
        #         if cols in col or ro-cols in negDiag or ro+cols in posDiag: continue
        #         col.add(cols)
        #         negDiag.add(ro-cols)
        #         posDiag.add(ro+cols)
        #         board[ro][cols]= "Q"
        #         backtracking(ro+1)
        #         col.remove(cols)
        #         negDiag.remove(ro-cols)
        #         posDiag.remove(ro+cols)
        #         board[ro][cols]= "."
        # backtracking(0)
        # return res


# curCur = ""
# for j in range(n):
#     curCur += "." if j!=i else "Q"


        # def backtracking(curr, i,k):
        #     if k >= n: 
        #         res.append(curr[:])
        #         return
        #     if curr and (curr[-1] in posDiag or curr[-1] in negDiag or curr[-1] in col): 
        #         return
        #     curr.append((i,k))
        #     posDiag.add(curr[-1])
        #     negDiag.add(curr[-1])
        #     col.add(curr[-1])
        #     backtracking(i+1, curr,k+1)
        #     curr.pop()
        #     posDiag.remove(curr[-1])
        #     negDiag.remove(curr[-1])
        # #     col.remove(curr[-1])

        # #     backtracking(i+1, curr,k+1)
        # # backtracking([],0,0)
        # return res