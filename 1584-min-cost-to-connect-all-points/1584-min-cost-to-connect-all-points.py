class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adjList = defaultdict(list)
        for i in range(len(points)):
            for j in range(len(points)):
                if i == j: continue
                manDist = abs(points[i][0]- points[j][0]) + abs(points[i][1]- points[j][1])
                adjList[tuple(points[i])].append((tuple(points[j]),manDist))
        res = 0
        minHeap, visited = [(0,tuple(points[0]))], set()
        while minHeap:
            val, point = heapq.heappop(minHeap)
            if point in visited: continue
            visited.add(point)
            res += val
            for node, dist in adjList[point]:
                if node not in visited:
                    heapq.heappush(minHeap, (dist,node))
        return res




#         return res

# [[0,0],[2,2],[3,10],[5,2],[7,0]]

# adj list with having source having everything as neighbor and then using MST off that


# 0:[(2,2),... 3,5]
# #kruskals (use when sparse e.g vertices are more than 2x than edges  ) mlogn because youre sorting 
# #prim's dense graphs mlogn (more optimal) 1. 