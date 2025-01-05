class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return 0
        res = float('-inf')
        # sliding window
        # brute o n2
        maxsub = [] 
        prefixSum =0
        l,r = 0,0
        while r < len(nums):
            prefixSum += nums[r] 
            res = max(prefixSum,res)
            if(prefixSum>= 0):
                r +=1
            else:
                prefixSum =0
                r+=1
                l = r
            
        return res
            
        # prefixSum = 0
        # for i in range(len(nums)):
        #     curSum = 0
        #     for j in range(i, len(nums)):
        #         # print(self.sum1([1,2]))
        #         curSum += nums[j]
        #         # res = max(res, sum(nums[i:j+1]))
        #         res = max(curSum,res)
        # return res