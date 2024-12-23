class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = cost.copy()
        # print(dp)
        dp.append(0)
        # print(dp)
        # dp[len(cost)] = 0

        for idx in range(len(dp)-3,-1,-1):
            dp[idx] = min(dp[idx] + dp[idx+1], dp[idx] + dp[idx+2])
        return min(dp[0],dp[1])



        for i in range(5,1,-1):
            print(i)
