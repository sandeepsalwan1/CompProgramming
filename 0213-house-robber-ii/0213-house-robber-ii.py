class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def dp(i,v):
            if i>= len(v):return 0
            return max(dp(i+1, v), v[i]+dp(i+2,v))
        
        return max(nums[0],dp(0, tuple(nums[:-1])), dp(0, tuple(nums[1:])))























        # @cache
        # def dp(i,newNums):
        #     if i>= len(newNums): return 0
        #     return max(dp(i+1, newNums), newNums[i] + dp(i+2, newNums))
        # storedNum1, storedNum2 = tuple(nums[1:]), tuple(nums[:-1])
        # return max(nums[0],dp(0, storedNum1), dp(0, storedNum2))

        # def helper(num):
        #     rob1, rob2= 0,0
        #     for n in nums:
        #         newVal = max(rob1, rob2+n)
        #         rob1 = rob2
        #         rob2 = newVal
        #     return rob2
        # @
        # def help(num):


        # return max(helper(nums[1:]), helper(nums[:-1]), nums[0])