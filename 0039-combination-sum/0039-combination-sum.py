class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # subset,res = [],[]
        res = []
        def backtracking(i, subset, sumVal):
            if  sumVal == target: 
                res.append(subset[:])
                return
            if( i >= len(candidates))or sumVal > target:
                return

            subset.append(candidates[i])
            backtracking(i, subset, sumVal+ candidates[i])
            subset.pop()
            backtracking(i + 1, subset, sumVal)

        backtracking(0,[],0)
        return res