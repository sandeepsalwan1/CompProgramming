class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid),len(grid[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        seen = set()

        def bfs(r,c):
            q = deque([[r,c]])
            grid[r][c]=0
            res = []
            while q:
                for i in range(len(q)):
                    ro,co = q.popleft()
                    res.append([ro,co])
                    for dr,dc in directions:
                        ra,ca = ro+dr, co+dc
                        if( ra in range(0,ROW) 
                            and ca in range(0,COL) 
                            and grid[ra][ca] == 1):
                            q.append([ra,ca])
                            grid[ra][ca]=0
                            seen.add((ra,ca))
            return res
        visited = set()
        def dfs(r,c):
            if not(r in range(0,ROW) 
            and c in range(0,COL) and grid[r][c]==1 
            and (r,c) not in seen and (r,c) not in visited):
                return
            grid[r][c]=0
            visited.add((r,c))
            for dr,dc in directions:
                dfs(r+dr,c+dc)
        self.cur =[]
        def bfs1():
            q = deque(visited)
            # res = []
            # print(self.cur,"a")
            level =0
            print(q)
            while q:
                for i in range(len(q)):
                    ro,co = q.popleft()
                    if grid[ro][co]==1: return level -1
                    for dr,dc in directions:
                        ra,ca = ro+dr, co+dc
                        if( ra in range(0,ROW) 
                            and ca in range(0,COL) 
                            and (ra,ca) not in seen):
                            q.append([ra,ca])
                            seen.add((ra,ca))
                level+=1
            return res
        self.cur =0  

        # lists =[]
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c]==1:
                    dfs(r,c)
                    return bfs1()
                else:
                    seen.add((r,c))

        # print(lists)
        # minDist = float('inf')
        # for a,b in lists[0]:
        #     for c,d in lists[1]:
        #         minDist = min(minDist, (abs(c-a) + abs(d-b)))
        # return minDist-1
        # 0,0 1,0

        # 0,1. 

        #     3,2
        # 3,3 2,3