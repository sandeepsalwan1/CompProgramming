# [7,1,5,3,6,4]


# prices[l] < prices[r]: l+=1



# [7,1,5,-3,6,4]

#         l
#           r

#    maxPrice = r-l
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # if len(prices)==1 : return 0
        res = 0
        l,r =0, 1 
        while r < len(prices):
            if prices[r] < prices[l]:
                l=r
            res = max(res, prices[r]-prices[l])
            r+=1

        return res


















#         l,r = 0, 1
#         res = 0
#         while r < len(prices):
            
#             if prices[l] < prices[r]: res = max(prices[r]-prices[l], res)
#             else: l=r
#             r+=1
#         return res
        
        
        
        
        
        
        
        
# #         [5,1, 10, 6] 

# l 1
# r 10

# 9
# #         1
# #         5
# #         -4
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# #                l,r,res = 0, len(prices)-1, 0 
# #         maxRight = 0
# #         minLeft = prices[0]
# #         while l < r: 
# #             if prices[l]> prices[r]: 
# #                 l+=1
# #                 minLeft = min(minLeft, prices[l])

# #             else: 
# #                 maxRight = max(prices[r], maxRight)
# #                 r-=1
# #             res = max(res, prices[r] - prices[l], maxRight - prices[l], prices[l]- minLeft, prices[r]-prices[l] )

# #         return res



# # #        l            
# # #         r
# # # [7,2,5, 1 3,6,4]



# # #         l            
# # #           r
# # # [7,2,5, 1 3,6,4]
          
# # # [7,6,4,3,1]

















# # #         # l,r = 0, 1
# # #         # maxVal = 0
# # #         # while r < len(prices):
# # #         #     if prices[r] > prices[l]:
# # #         #         maxVal = max(prices[r] -prices[l],maxVal)
# # #         #     else:
# # #         #         l = r
# # #         #     r+=1
# # #         # return maxVal

