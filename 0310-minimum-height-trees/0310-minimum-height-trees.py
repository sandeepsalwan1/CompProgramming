class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        adj = defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        edge_cnt = {}
        mainLeaves = deque()

        for src, neighbors in adj.items():
            edge_cnt[src] = len(neighbors)
            if len(neighbors) == 1:
                print('a')
                mainLeaves.append(src)

        while mainLeaves:
            if n <= 2:
                return list(mainLeaves)
            for _ in range(len(mainLeaves)):
                node = mainLeaves.popleft()
                n -= 1
                for nei in adj[node]:
                    edge_cnt[nei] -= 1
                    if edge_cnt[nei] == 1:
                        mainLeaves.append(nei)