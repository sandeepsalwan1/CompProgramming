class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset,res = [],[]

    #12 
    #. 
        def backtracking(i):
            if i == len(nums): 
                res.append(subset.copy())
                return
            subset.add(nums[i])
            backtracking(i+1)

            subset.pop()
            backtracking(i+1)


        backtracking(0)