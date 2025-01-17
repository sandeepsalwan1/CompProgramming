class Solution:

    # basecase: the robber is [1,2,3,1]
    # 2 cases: 
    # take = max(nums[i]+nums[i+2], nums(i+1)), i < len(nums)
    # stay = 0+1, i+1




    def rob(self, nums: List[int]) -> int:
        @cache
        def recursive(i):
            if  i >= len(nums): return 0
            return max(recursive(i+1), recursive(i+2) + nums[i])
            # take = 0

            # stay = recursive(i+1, x)
        return recursive(0)
        # robber1,robber2 = 0,nums[0]

        # for i in range(1,len(nums)):
        #     robber1, robber2 = robber2, max(robber2, robber1+ nums[i])
        
        # return robber2
        
"""

"""
