class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res = 0
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if r-c==0:
                    res += mat[r][c]
                    continue
                if r+c==len(mat)-1:
                    res += mat[r][c]

        return res