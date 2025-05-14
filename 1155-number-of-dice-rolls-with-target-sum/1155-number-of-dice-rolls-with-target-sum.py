class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        @lru_cache(maxsize=None)
        def dfs(used, target):
            if used == n:
                return 1 if target == 0 else 0

            count = 0
            for face in range(1, k+1):
                count += dfs(used + 1, target - face)

            return count % (10**9 + 7)

        return dfs(0, target)
        