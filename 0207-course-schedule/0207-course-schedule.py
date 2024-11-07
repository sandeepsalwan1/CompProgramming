class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited, cycle = set(), set()
        preqDict =defaultdict(list)
        [preqDict[pre].append(crs) for pre,crs in prerequisites]
        print(preqDict)
        def dfs(crs):
            if crs in cycle: 
                return False
            if crs in visited: 
                return True 
            cycle.add(crs)
            for pre in preqDict[crs]:
                if not dfs(pre): return False
            cycle.remove(crs)
            visited.add(crs)
            return True
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True
        