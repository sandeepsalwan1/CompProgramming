# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
# #         self.right = right


# #dfs  

# do dfs on every node

# dfs bottom up

# dfs(node, direction)

# return max(1+ dfs(node.left,not direction),  1+ dfs(node.right,not direction))

# O(v+e) 
# o(n^2)
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        # self.maxLen = 0

        @cache
        def dfs(node, lastInputLeft, depth):
            if not node: return depth

            if lastInputLeft:
                depth = max(
                    depth,
                    dfs(node.right,False,depth+1),
                    dfs(node.left,True,0)
                )
            else:
                depth = max(
                    depth,
                    dfs(node.left,True,depth+1),
                    dfs(node.right,False,0)
                )
            return depth

        return max(dfs(root.left,True,0), dfs(root.right,False,0))
#         def dfs(node,leftTrue):
#             if not node: return 0
#             takeRight = 1+ dfs(node.right, False) if node.right else 0 
#             takeLeft = 1+ dfs(node.left,True) if node.left else 0 
            
#             self.maxLen = max(self.maxLen, takeLeft, takeRight)
            
#             if leftTrue: 
#                 takeLeft = 0
#             else:
#                 takeRight = 0
#             return max(max(dfs(node.left,True),dfs(node.left,False) if node.left else 0),
#             max(dfs(node.right,True),dfs(node.right,False) if node.right else 0), takeLeft, takeRight)

#         # val = 0
#         # if (root.left and not root.right): val = 1
#         if not root: return 0
#         max(dfs(root, True), dfs(root, False))
#         return self.maxLen

# #      1

# #          1
# #         1   1
# # 0              1

#     #    1
