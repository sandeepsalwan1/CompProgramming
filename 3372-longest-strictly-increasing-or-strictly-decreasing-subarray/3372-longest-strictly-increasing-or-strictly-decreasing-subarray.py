'''        sliding window four pointer resets if curr isnt increasing/decreasing
'''

# 1 4 3 3 2
        #   l r
#  increasingCount = 2
#  decreasingCount = 1


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        resIncreasingCount, resDecreasingCount = 1,1
        increasingCount, decreasingCount = 1,1
        lIncreasing, rIncreasing = 0,1
        lDecreasing, rDecreasing = 0,1
        while rIncreasing < N:
            if nums[rIncreasing] > nums[lIncreasing]:
                increasingCount +=1
            else: 
                increasingCount = 1

            if nums[rDecreasing] < nums[lDecreasing]:  
                decreasingCount +=1
            else:
                decreasingCount = 1

            resIncreasingCount = max(resIncreasingCount, increasingCount)
            resDecreasingCount = max(resDecreasingCount, decreasingCount)
            rIncreasing, rDecreasing = rIncreasing + 1, rDecreasing +1
            lIncreasing, lDecreasing = lIncreasing + 1, lDecreasing +1
        return max(resIncreasingCount, resDecreasingCount)
