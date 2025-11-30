class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        res =0
        count1 = defaultdict(int)
        l,r = 0,0
        while r < len(nums):
            count1[nums[r]]+=1
            while count1[nums[r]] > k:
                count1[nums[l]]-=1
                l+=1
            res = max(res, r-l+1)
            r+=1
                
        return res

        # [1,2,3,1,2,3,1,2]
        #                r
        #    l 
        # 1:2,2:2,3:2