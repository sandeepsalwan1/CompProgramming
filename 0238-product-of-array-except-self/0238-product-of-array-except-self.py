# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         #brute would be double for loop  on^2 on space
#         sumVal = 1
#         withZeroVal = 1
#         count = 0
#         for i in nums: 
#             if count == 1:
#                 withZeroVal *= i
#             if i == 0: 
#                 count += 1
#                 withZeroVal = sumVal
#             sumVal *= i

#         res = []
#         for i in nums:
#             if i == 0:
#                 if count == 1:
#                     val = int(withZeroVal)
#                 else:
#                     val = int(sumVal)
#             else:
#                 val = int(sumVal/i)
#             res.append(val)
#         return res

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res