# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        curLis = []
        def bfs(cur):
            q = deque([cur])
            while q:
                cur = []
                for i in range(len(q)):
                    child = q.popleft()
                    if child.left: q.append(child.left)
                    if child.right: q.append(child.right)
                    cur.append(child.val)
                curLis.append(cur)
        bfs(root)
        
        return curLis[-1][0]

        