class Solution:
    def climbStairs(self, n: int) -> int:
        @cache  
        def fib(i):
            if i <= 1: return i
            return fib(i-1)+ fib(i-2)
        
        return fib(n+1)
        # one,two = 1,1
        # for i in range(n-1):one,two = one+two,one
        # return one
        # # if n <= 2: return n
        # # # dp = [0] * n
        # # dp[-1],dp[-2] = 1,2
        # prev, prevPrev = 2,1
        # res = 0
        # for i in range(2,n):
        #     # print(res,prev,prevPrev)
        #     res = prev + prevPrev
        #     prevPrev, prev = prev, res
        #     # print("yo",res,prev,prevPrev)

        # return res
        # # # [2,1,1]
        # # print(dp)
        # # for i in range(len(dp)-3,-1,-1):
        # #     dp[i] = dp[i+1] + dp[i+2]
        # # print(dp)
        
        # # return dp[0]
