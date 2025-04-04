# insert in any order so I will 

# start 

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        output = [list(itertools.combinations(nums,i)) for i in range(len(nums) + 1)]
        for i in output:
            for j in i:
                res.append(j)
        return res
#         self.output = []
#         def backtracking(i,cur):
#             if not cur: return [[]]
            

#         backtracking[0, nums]
#         return self.output

# base case: i >= len(nums)


# backtrack approach:
# self.output = []
# backtracking(i+1, cur)
# cur.append(nums[i])
# if not cur: return [[]]
# cur.popleft()
# for loop
# backtracking(i+1, cur)

# cur.append()
# [3]




# f1 
# 123


# f2 
# 23

# f3 
# 2, 3




# 3


# 13


# 32