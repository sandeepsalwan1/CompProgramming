class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # res = []
        # [1,2,3]
        subset = []
        res = []
        def dfs(i):
            if i -= len(nums):
                res.append(subset.copy())
                return 
            subset.append(nums[i])
            dfs(i+1)

            subset.pop()
            dfs(i+1)
        dfs(0)
        return res

        # def backtracking(input):
        #     if input 
        #     for i in input:
        #         if i == 0:
        #             return
        # def testBack():

                   
        # return backtracking(nums)