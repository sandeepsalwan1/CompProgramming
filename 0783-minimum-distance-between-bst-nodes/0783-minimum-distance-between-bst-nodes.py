
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        ans = float('inf')
        self.prev = None
        def dfs(node):
            nonlocal ans
            if not node:
                return
            # if self.prev
            dfs(node.left)

            if self.prev:ans = min(ans, node.val - self.prev.val)
            self.prev = node

            # if preve:
            dfs(node.right)


        dfs(root)
        return ans

# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def minDiffInBST(self, root: Optional[TreeNode]) -> int:
#         self.first, self.second  = -10000, float('inf')
#         # curLis = []
#         self.prevRes = float('inf')
#         def dfs(cur,prev):
#             if not cur: return 0
#             dfs(cur.left,cur.val)
#             self.prevRes = min(abs(prev-cur.val), self.prevRes)
            
#             dfs(cur.right,cur.val)
#         dfs(root, float('inf'))
#         # for i in range(len(curLis)-1):
#         return self.prevRes
#         # print(second-first)
#         def bfs(cur):
#             q = deque([cur])
#             # seen = se
#             while q:
#                 for i in range(len(q)):
#                     child = q.popleft()
#                     if child.left: q.append(child.left)
#                     if child.right: q.append(child.right)
#                     print(self.first,self.second)
#                     if abs(child.val - self.first) < abs(self.second - self.first):
#                         self.first,self.second = child.val,self.first
#                     print(self.first,self.second)
                
#             return abs(self.second - self.first)
#         return bfs(root)