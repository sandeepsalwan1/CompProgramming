# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        curLis = []
        def findHeight(curr):
            if not curr: return 0
            return 1 + max(findHeight(curr.left), findHeight(curr.right))
        maxHeight = findHeight(root)
        print(maxHeight)
        
        def bfs(cur):
            q = deque([cur])
            level = 1
            while q:
                cur = []
                print(level)
                for i in range(len(q)):
                    child = q.popleft()
                    if child.left: q.append(child.left)
                    if child.right: q.append(child.right)
                    if level == maxHeight: return child.val
                # curLis.append(cur)
                level+=1
        print(bfs(root))
        return bfs(root)
        
        return curLis[-1][0]

        