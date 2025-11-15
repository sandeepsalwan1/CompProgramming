# Definition for a binary tree node.
# class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right




#     #       3
#     #     1   4
#     #   3    1  5


# #o(b*h)
# #O(2^log(n))
# #o b*m
# o(n)
# o(n)
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res =0 
        def dfs(cur, maxV):
            if not cur: return
            if cur.val >= maxV:
                self.res +=1
            maxV = max(maxV, cur.val)
            dfs(cur.left,maxV)
            dfs(cur.right,maxV)


        dfs(root, float('-inf'))
        return self.res

# no node greater= maxV






#   Non          O               O          O             O
#                             O               O          O. O

                            
# 0            True          



















        # # dfs and check at every iteration if greater than currMax
        # if not root: return 0
        # self.res = 0
        # def dfs(curr,currMax):
        #     if not curr: return 
        #     if curr.val >= currMax: self.res +=1
        #     # newMax = max(currMax, curr.val)
        #     dfs(curr.left, max(currMax, curr.val))
        #     dfs(curr.right, max(currMax, curr.val))

        # dfs(root,root.val)
        # return self.res
