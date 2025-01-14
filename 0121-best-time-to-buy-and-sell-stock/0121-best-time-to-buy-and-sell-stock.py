class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0, 1
        maxVal = 0
        while r < len(prices):
            if prices[r] > prices[l]:
                maxVal = max(prices[r] -prices[l],maxVal)
                # r+=1
            else:
                l = r
            r+=1
        return maxVal