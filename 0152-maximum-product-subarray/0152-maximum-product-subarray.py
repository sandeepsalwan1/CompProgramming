'''


2 3 -2 -4

2 6  -2  -4* -2, -4*-12, -4

1 1  -12 


Our approach would be to take the current max/min product of everything.
this is because lets say we have 1,2,3. we simply return the max product
which is [1,2,6]. we se that max would be largest here so we just return the 6.

In the case we have  [-4,-5,6]
-4 * -5 * -6 0 -2

max: -4   20    30  0   2 
min: -4.  -5    -120  0  0

'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        for i in range(len(nums)):
            currSub = 1
            for j in range(i,len(nums)):
                currSub *= nums[j]
                res = max(res,currSub)
        return res
        # prodSum =[]
        minVal, maxVal = 1,1
        res = max(nums)
        for n in nums:
            tmp = maxVal * n
            maxVal = max(tmp, minVal*n, n)                       
            minVal = min(tmp, minVal*n, n)
            res = max(res, maxVal)

        return res

# o(n)
# o(1)