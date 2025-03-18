class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        res= 1
        l = 0
        cur = 1
        for r in range(len(nums)):
            if nums[l]&nums[r] == 0: 
                cur +=1
                res = max(cur,res)
            else: 
                cur = 1
                l = r
        return res

        # 11
