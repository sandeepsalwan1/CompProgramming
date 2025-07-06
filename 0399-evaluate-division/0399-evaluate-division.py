class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Step 1: Create weighted graph
        checkDict = {}
        for i in range(len(equations)):
            a, b, c = equations[i][0], equations[i][1], values[i]
            if a not in checkDict:
                checkDict[a] = {}
            checkDict[a][b] = c
            if b not in checkDict:
                checkDict[b] = {}
            checkDict[b][a] = 1/c
        
        print(checkDict)
        # Step 2: Traver the queries and get the value
        res = []
        # def dfs(a1,b1, val):
        #     if f not 
        def bfs(a1,b1):
            seen = set()
            queue = deque([[a1, 1]])
            seen.add(a1)
            while queue:
                for i in range(len(queue)):
                    cur, v = queue.popleft()
                    if cur == b1:
                        return v
                    for child in checkDict[cur]:
                        if child not in seen:
                            seen.add(child)
                            queue.append([child, v * checkDict[cur][child]])
            return -1

        for a,b in queries:
            if a not in checkDict or b not in checkDict: 
                res.append(-1.0)
            elif a == b:
                res.append(1)
            else:
                res.append(bfs(a, b))

        return res
