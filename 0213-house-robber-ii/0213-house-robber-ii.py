class Solution:
    def rob(self, nums: List[int]) -> int:
        # if(len(nums)):
        def robberMain(nums):
            robber1,robber2 = 0,0
            for n in nums:
                robber1,robber2 = robber2, max(n+ robber1, robber2)
            return robber2
        return max(robberMain(nums[1:]), robberMain(nums[:-1]), nums[0])