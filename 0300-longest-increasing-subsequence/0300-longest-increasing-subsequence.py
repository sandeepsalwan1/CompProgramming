# include or not include
#            [1]           [2] [5] [4]
#     [1,2]  [1,5] [1,4]

# [1,2,5] [1,2,4]
        # currVal = nums[0]
        # self.res = 1

        # OPT = [1] * len(nums)

        # for i in range(len(nums) -1,-1,-1):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] < nums[j]:
        #             OPT[i] = max(OPT[i], 1 + OPT[j])
        # return max(OPT)
# from functools import *
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        if N <= 1: return N
        @cache
        def recursive(i):
            best = 1
            for j in range(i+1, N):
                if nums[j] > nums[i]:
                    best = max(best, 1+ recursive(j))
            return best
            # if nums[n] > currCounter: return False
            # currCounter+=1
            # self.res +=1
            # if  
            # skip = (i+1, n)
            # return recursive(n) + 

        return max((recursive(i)) for i in range(N))
        
        # recursive(0,0)
        # return self.res