class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        def dfs(alice, i, M):
            if i >= len(piles): return 0

            res = 0 if alice else float('inf')
            total = 0

            for X in range(1, 2*M+1):
                if i+X-1>=len(piles):break
                total += piles[i+X-1]
                if alice:
                    res = max(res,total+dfs(not alice,i+X, max(M,X)))
                else:
                    res = min(res,dfs(not alice,i+X, max(M,X)))

            return res



# [1,2,100]

# alice
# 1
#    0

        return dfs(True,0,1)