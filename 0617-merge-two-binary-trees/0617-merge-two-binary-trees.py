# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2: return None

        v1 = root1.val if root1 else 0
        v2 = root2.val if root2 else 0

        root = TreeNode(v1+v2)
        root.left = self.mergeTrees(root1.left if root1 else None,root2.left if root2 else None )
        root.right = self.mergeTrees(root1.right if root1 else None,root2.right if root2 else None )
        return root


        # def dfs(curr):

        # def bfs(cur):
        #     q = deque([cur])
        #     res = []
        #     while q:
        #         for i in range(len(q)):
        #             child = q.popleft()
        #             if child:q.append(child.left)
        #             if child:q.append(child.right)
        #             if child: res.append(child.val)
        #             else: res.append(None)


        #     return res
        
        # lis1,lis2 = bfs(root1), bfs(root2)
        # maxV = 0
        # maxV = len(lis1) if len(lis1) > len(lis2) else len(lis2)
        # print(maxV,lis1,lis2)
        # res = []
        # i,j = 0,0
        # while i < len(lis1) and j < len(lis2)
