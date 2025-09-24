class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]*(i+1) for i in range(numRows)]
        print(res)
        for r in range(2,numRows):
            for c in range(1,r):
                res[r][c] = res[r-1][c-1] + res[r-1][c]

      
        return res
        # for i in range(1,numRows):
        
        # return res