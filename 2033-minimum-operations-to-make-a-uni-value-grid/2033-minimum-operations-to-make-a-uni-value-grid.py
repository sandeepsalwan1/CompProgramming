# #greedy is good for min


# 2+ 2 

# 6-2 

# [2,4],[6,8]

# 8 - 2*2

#   6

#   4 

#     # elif x[i] == target continue
 

#     8-6
#     2/2

#     6-8

# list and sort them. because we're choosing (median is term in odd lists but not even) middle val in sorted list. 

# iterate through
# if val < target res += abs(target-x[i]) / xVal
# else: continue
# TC: O(n*m (log(m*n))) SC: O(m*n)
# return res
#   k
# calc time to get to that mid val [2,4,6,8] mid val 

# [1,2][999,1000] x = 997



# [2] [6] x =2

#  goal: 2

#  ops: 2 6-2*2




# invalid?

# [[1,2],[3,4]], x = 2

# [1 %2,2 %2] . not possible two make two integers equal if different mod result 
# 2%2, if two parities are differente then invalid 




        # midList = [j for j in i for i in grid]
        # if len(grid) == 1: return 0
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        midList, res = [], 0 
        curVal = grid[0][0] % x
        for i in grid:
            for j in i:
                if j%x != curVal: return -1
                midList.append(j)
        midList.sort()
        target = midList[(len(midList)//2)]
        for i in midList:
            res += abs(target-i) // x
        return res
        # print(midList)