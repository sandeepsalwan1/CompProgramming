# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# '''
# root


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diam = 0
        def dfs(cur):
            if not cur:
                return 0
            left, right = 1+ cur.left,  1+ cur.right
            self.diam = max(self.diam, left+right)
            # dfs()


        dfs(root)
        return self.diam
























# depth 1 = 0 

# everytime we iterate we add 1 to depth 
# maxDiam = 0
# dfs params: curr, diam

# everytime we iterate to left/right we'll add 1 to diam
# every iteration we'll compare maxDiam with curr depth

# '''

#        1
#       2.  3
# #     4. 5


#     1 
#      2

#     f1 
#        dfs(2) 
                        
#         1 + left,right  
    
#      we do 
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diam = 0
        def dfs(cur):
            if not cur: return 0
            l,r = dfs(cur.left), dfs(cur.right)
            self.diam = max(self.diam, l+r)
            return 1 + max(l,r)
        dfs(root)
        return self.diam










        self.maxDiam = 0
        def dfs(curr):
            if not curr: return 0
            print(curr.val)
            left, right = dfs(curr.left), dfs(curr.right)
            self.maxDiam = max(self.maxDiam, left + right)
            return 1+ max(left, right)

        dfs(root)
        return self.maxDiam


    #  1 
     

        # 5


    #  3.   1

    #





        # 1 

#       2. 3
#     4.  5
  # 8  


    #   2
    # 1 
     
# 4= 1 
# r = 1 1



#     #    check height and depth as we go
#         res = 0
#         def dfs(root):
#             nonlocal res
#             if not root: return 0
#             left = dfs(root.left)
#             right = dfs(root.right)
            
#             res = max(res, left+right)
#             return max(left, right) +1
#         dfs(root)
#         return res

#     #     1
#     #    2 3.            
#     #   4 5

#     #     1
#     #    2
       
       
#         # self.maxDiam = 0
#         # # height = max(l,r) + 1
#         # def dfs(curr):
#         #     if not curr: return -1
#         #     left = dfs(curr.left)
#         #     right = dfs(curr.right) 
#         #     diam = left + right+ 2 
#         #     self.maxDiam = max(self.maxDiam, diam)
#         #     return 1+ max(left, right)
#         # dfs(root)
#         # return self.maxDiam


#         # dfs(root,0)
#         # return self.maxDiam