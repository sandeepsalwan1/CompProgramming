class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res, cur = [],[]
        def backtracking(i,curVal):
            if i >= len(candidates) or curVal> target: return
            if curVal == target: 
                res.append(cur.copy())
                return
            cur.append(candidates[i])
            backtracking(i, curVal + candidates[i])
            cur.pop()
            backtracking(i+1, curVal)
        
        backtracking(0,0)
        return res

#                 2   
#             2     27mk,                                                                                           
#         2 6
#     2    2223
# 2       



















#         res =[]
#         numberTimes = target//min(candidates) + 1
#         while numberTimes > 0:  
#             for p in itertools.product(candidates, repeat = numberTimes):
#                 if sum(p) == target: 
#                     val = list(p)
#                     val.sort()
#                     if val not in res:
#                         res.append(val)

#             numberTimes -=1
#         return res













#         # stack = []
#         # res = []

#         # def combination(idx, val):
#         #     if idx >= len(candidates) or val >= target: return
#         #     if val == target: 
#         #         res.append(stack.copy()) 
#         #         return
            
#         #     stack.append(candidates[idx])
#         #     combination(idx, val+ candidates[idx])
#         #     stack.pop()
#         #     combination(idx+1, val - candidates[idx])

#         # combination(0,0)
#         # return res