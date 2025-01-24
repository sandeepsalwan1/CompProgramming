# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



# dfs and Recursively call Same Tree function


# TreeNode(3,None)

#         root
#           1
#          2 4           
#         3 5 
        
#                           root, subRoot
#                           edge cases
#                           if no subroot; true
#                           if no root is: false
#                           if is SameTree(first,second): return true
#                           def isSameTree()
#                             if not first and not second: return True
#                             if not first or not second: return False
#                             if first.val != second.val: return False
#                             return SameTree(first.left, second.left) and
#                                 SameTree(first.right, second.right)

#                           return root.left,subtree or root.right, subtree
#     subRoot
#          2 
#         3 5


'''
             3
           4   6
         1.  2 
     null null 






same tree params: first, second
    if not first and not second: return True 
    if not first or not second: return False 
    if first.val != second.val: return True
    return sameTree(first.left, second.left) and sameTree(first.right, second.right)
if not subRoot: return True
if not root: return False
if sameTree()
# return root.left and root.right 
root.left and subtree
'''
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(first, second):
            if not first and not second: return True 
            if not first or not second: return False 
            if first.val != second.val: return False
            return sameTree(first.left, second.left) and sameTree(first.right, second.right)
        if not subRoot: return True
        if not root: return False
        if sameTree(root,subRoot): return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot) 