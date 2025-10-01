# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root.val == 0: return False
        if root.val == 1: return True

        def dfs(cur):
            if not cur: return
            if not cur.left and not cur.right: return cur.val
            first = dfs(cur.left)
            second = dfs(cur.right)
            # dfs(cur.left)
            # dfs(cur.right)
            first = True if first == 1 else False
            second = True if second == 1 else False
            print(first,second)
            if cur.val ==2:
                return first or second
            else:
                return first and second
            # if first == 
        return dfs(root)
