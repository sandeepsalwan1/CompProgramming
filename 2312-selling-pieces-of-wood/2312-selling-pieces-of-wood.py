class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        priceMap = {}
        for h,w,p in prices:
            if h in priceMap:
                priceMap[h][w] = p
            else:
                priceMap[h] = {w:p}
        # print(priceMap)

        def getPrice(h,w):
            if h in priceMap and w in priceMap[h]:
                return priceMap[h][w]
            return 0

        @cache
        def dp(a,b):
            money = getPrice(a,b)
            for h in range(1,a):
                money = max(money, dp(h,b) + dp(a-h,b))
            for w in range(1,b):
                money = max(money, dp(a,w) + dp(a,b-w))

            return money

        return dp(m,n)
        # 1 
        # 2
        # 3

        # {h: {w: k}}
        # 1,5

        # 1,h
        # 1,5 

        # 2,5



        # 1,4 2,2 2,1

