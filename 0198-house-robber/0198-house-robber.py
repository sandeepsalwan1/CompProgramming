class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def dp(i):  
            if i >= len(nums):
                return 0 
            return max(nums[i] + dp(i+2), dp(i+1))

        return dp(0)




















        @cache
        def dp(i):
            if i>= len(nums): return 0
            return max(dp(i+2)+nums[i], dp(i+1))
        return dp(0)



























        def dp(i):
            if i>= len(nums):
                return 0
            return max(dp(i+1), nums[i]+dp(i+2))
        return dp(0)

# 0

#  [100,2,3,100]
#                                  i0     
#                               0           1 i2                    i
#                             i1                               i2 
#                         0                                         4
#                     0 i2                           i3         i3           i4
#                 0                              2      4
#             i3           3 i4       
#         0         
# i4              1 i5  


# f4- max:1


# dp(3), nums[2]+ dp(4)

# max(1,3) = 3


















#     # basecase: the robber is [1,2,3,1]
#     # 2 cases: 
#     # take = max(nums[i]+nums[i+2], nums(i+1)), i < len(nums)
#     # stay = 0+1, i+1




#     def rob(self, nums: List[int]) -> int:
#         # res = 0
#         # case: take or stay 
#         @cache
#         def take(i):
#             if  i >=                          xxxxxxxxxx len(nums): return 0
#             return max(nums[i]+ take(i+2), take(i+1))
#             # take = nums[i] + nums[i+2]
#             # stayVal = take[i+1]
#             # return max(takeVal, stayVal)
#         return take(0)

        















#         @cache
#         def recursive(i):
#             if  i >= len(nums): return 0
#             return max(recursive(i+1), recursive(i+2) + nums[i])
#             # take = 0
#             # stay = recursive(i+1, x)
#         return recursive(0)
#         # robber1,robber2 = 0,nums[0]

#         # for i in range(1,len(nums)):
#         #     robber1, robber2 = robber2, max(robber2, robber1+ nums[i])
        
#         # return robber2
        
# """

# """




