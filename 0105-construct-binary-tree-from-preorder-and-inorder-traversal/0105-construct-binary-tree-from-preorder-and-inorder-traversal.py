# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder: return
        mid = inorder.index(preorder[0])
        root = TreeNode(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1],inorder[0:mid])
        root.right = self.buildTree(preorder[mid+1:],inorder[mid+1:])


        return root




#         3

#     9      20

#   1.    2   15    7
# 8

# 3 9  1 8 2 20 15 7 

# 8 1 9 2 3 15 20 7