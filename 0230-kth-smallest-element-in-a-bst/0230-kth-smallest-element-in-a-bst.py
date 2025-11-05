


















# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        self.res= 0
        def dfs(cur):
            nonlocal k
            if not cur: return
            dfs(cur.left)
            if k==1:
                k-=1
                self.res= cur.val
            k-=1
            dfs(cur.right)
            return self.res
        return dfs(root)



        

        # def dfs(cur):
        #     nonlocal k
        #     if not cur: return
        #     dfs(cur.left)
        #     if k == 1:
        #         k-=1
        #         return cur.val
        #     k-=1
        #     dfs(cur.right)
        # return dfs(root)











        def dfs(curr):
            nonlocal k
            if not curr: 
                return
            dfs(curr.left)
            print(k)
            if k == 1: 
                k-=1
                print(curr.val)
                return curr.val
            k-=1
            dfs(curr.right)
        return dfs(root)


























        self.val = k
        self.list = []
        self.res = None
        self.count = 0
        def dfs(curr):
            if not curr or self.res: return 
            dfs(curr.left)
            # self.list.append(curr.val)
            self.count +=1
            if self.count == k: 
                self.res = curr.val
                return
            dfs(curr.right)

        dfs(root)
        # return self.list[k-1]
        return self.res