# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def bfs(cur):
            seen = set()
            q = deque([cur])
            while q:
                cur =0 
                for i in range(len(q)):
                    child = q.popleft()
                    if child.left: q.append(child.left)
                    if child.right: q.append(child.right)
                    cur+=child.val
                # print(cur,res)
                res.append(cur)
                # print(cur,res)
        bfs(root)


        res.sort()
        # print(res)
        return res[-k] if k<= len(res) else -1

        