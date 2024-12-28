# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder: return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root

        
        # dfs left and right to  
        # # 3 is root. put the root as node. then observe that inorder[-1] is rightmost node and inorder[-2] os parent 
        # res = []
        # root = TreeNode(preorder[0])
        # mid = inorder.index(preorder[0])
        # root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        # root.right =self.buildTree(preorder[mid+1:],inorder[mid+1:] )
        # return root
        # # def dfs(curr, left, right):
        # #     print(curr)
        # #     # m = 

        # return res

            
            #    1
            #  2.  4
            # 3 7   5 6

            # pre: 1237456. in: 3271546