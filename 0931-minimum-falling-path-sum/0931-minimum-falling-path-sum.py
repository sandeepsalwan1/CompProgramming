class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        ROW, COL = len(matrix), len(matrix[0])

        @cache
        def dfs(r,c):
            if r== ROW: 
                return 0
            if c not in range(0,COL):
                return float("inf")
            return matrix[r][c] + min(
                dfs(r+1,c+1),
                dfs(r+1,c),
                dfs(r+1,c-1)
            )

            # return 
# 

        res = float('inf')
        for c in range(COL):
            res = min(res, dfs(0, c))
        return res

        
        directions = [[1,1], [1,0],[1,-1]]
        self.res = float('inf')
        def bfs(c):
            # q= deque([(0,c,0)])
            minV= [[matrix[0][c],0,c]]
            seen = set()
            while minV:
                for i in range(len(minV)):
                    # print(minV)
                    print(minV)
                    val = heapq.heappop(minV)
                    minV= []
                    # print(val)
                    cost,ro,co = val[0],val[1],val[2]
                    if ro == len(matrix)-1:
                        self.res = min(self.res,cost)
                        return
                    for dr,dc in directions:
                        if (dr+ro in range(0,ROW) 
                        and dc+co in range(0,COL) 
                        and (dr+ro, dc+co) not in seen):
                            # q.append([ro+dr, co+dc])
                            heapq.heappush(minV, [cost + matrix[ro+dr][co+dc], dr+ro,dc+co])
                            seen.add((ro+dr, co+dc))


        for c in range(COL):
            bfs(c)
            print(self.res,c)
        return self.res