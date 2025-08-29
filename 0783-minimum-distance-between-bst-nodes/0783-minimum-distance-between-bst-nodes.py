# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.first, self.second  = -10000, float('inf')
        curLis = []
        def dfs(cur):
            if not cur: return
            dfs(cur.left)
            curLis.append(cur.val)
            dfs(cur.right)
        dfs(root)
        prevRes = float('inf')
        for i in range(len(curLis)-1):
            prevRes = min(abs(curLis[i+1]-curLis[i]), prevRes)
        return prevRes
        # print(second-first)
        def bfs(cur):
            q = deque([cur])
            # seen = se
            while q:
                for i in range(len(q)):
                    child = q.popleft()
                    if child.left: q.append(child.left)
                    if child.right: q.append(child.right)
                    print(self.first,self.second)
                    if abs(child.val - self.first) < abs(self.second - self.first):
                        self.first,self.second = child.val,self.first
                    print(self.first,self.second)
                
            return abs(self.second - self.first)
        return bfs(root)