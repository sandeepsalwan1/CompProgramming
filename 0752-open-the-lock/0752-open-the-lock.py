class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        defDict = defaultdict(int)
        defDict["0"] = ["1","9"]
        defDict["9"] = ["8","0"]
        for i in range(1,9):
            defDict[str(i)] = [str(i+1),str(i-1)]
        # print (defDict)
        def bfs():
            val = "0000"
            if val in deadends:
                return -1 
            queue = deque([val])
            level = 0
            seen = set()
            seen.add(val)
            while queue:
                for i in range(len(queue)):
                    val1 = queue.popleft()
                    if val1 == target: 
                        return level
                    for j in range(4):
                        for k in defDict[val1[j]]:
                            t = list(val1)
                            t[j] = k
                            re= ''.join(t)
                            if re not in seen and re not in deadends:
                                seen.add(re)
                                queue.append(re)
                level += 1
            return -1
        return bfs()

        
        