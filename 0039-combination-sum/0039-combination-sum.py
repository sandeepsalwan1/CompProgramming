class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res, subset = [],[]
        def backtracking(i, sumVal):
            if i >= len(candidates) or sumVal > target: 
                return
            if sumVal == target:
                res.append(subset.copy()) # [:]
                return
            subset.append(candidates[i])
            backtracking(i, sumVal + candidates[i])
            subset.pop()
            backtracking(i + 1, sumVal)
        backtracking(0,0)
        return res

        # 2367
        # 2 2 2 3
        # res = 
        # i = 