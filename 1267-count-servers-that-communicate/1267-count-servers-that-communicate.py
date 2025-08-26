class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        res = 0
        # directions = [[1,0]]
        # def bfs(r,c):
        #     q = deque()
        #     seen = set()
        #     seen.add((r,c))
        #     while q:
        #         for i in range(len(q)):

        checkDict = defaultdict(int)
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    res +=1
                    checkDict["r"+str(r)] += 1
                    checkDict["c"+str(c)] += 1
        # print(res)
        # print(checkDict)
        for r in range(ROW):
            for c in range(COL):
                # print(r,c, not (checkDict["r"+str(r)] > 1 or checkDict["c"+str(c)] > 1))
                if grid[r][c] == 1 and not (checkDict["r"+str(r)] > 1 or checkDict["c"+str(c)] > 1):
                    res -=1

                    # if bfs(r,c): 
                    #     res += 1


        return res
                    
