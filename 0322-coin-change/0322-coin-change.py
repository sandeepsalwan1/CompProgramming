class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # if amount == 0 : return 0
        # self.res = float('inf')
        @cache
        def startWithToMake(i,x):
            if x == amount: 
                return 0
            if i >= len(coins): return float('inf')
            take = float('inf')
            if x + coins[i] <= amount:
                take = startWithToMake(i, x+ coins[i])   
                if take != float('inf'): take +=1
            skip = startWithToMake(i+1, x)
            return min(take,skip)
        self.res = startWithToMake(0,0)
        return self.res if self.res != float('inf') else -1
        
        
        """
        base case:
        take: 
            (i, x+ coins[i], i < len(coins))
        skip: 
            (i+1, x, i < len(coins))
        
        assume true at n 
        prove n = k+1
        divisibility/gcd 
"""