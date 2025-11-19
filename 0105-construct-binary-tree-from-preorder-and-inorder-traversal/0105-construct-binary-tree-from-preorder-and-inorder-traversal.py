# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right

#                   1
#               2.      3 
#             4.  5.   6. 7
#            8
#          9. 10


#         1
#        2


# 

# 
# class TreeNode:
#     def __init__(val = 0, left = None,right= None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder: return
        root = TreeNode(preorder[0])
        mid = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:mid+1],inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:],inorder[mid+1:])



        return root
# preorder = [3,9,20,15,7,12,15], inorder = [9,3,15,20,7,12, 15]


# preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]

# .left
# pre [9,20,15,7]

# in [9]
# root is 9
#     .left
#     pre[20,...]
#     in []
#     return so the root will eventually return 9


# .right
#     root = 20
#     mid = 1
#     pre[20,15,17]
#     inorder[20,15,17]
    
#         .left 
#             root = 15
#             mid = 1
#             pre[15]
#             inorder[20,15,17]



# # 3 is root . first index in preorder is root. 

# # 2. left of index at which preorder[0] is in at inorder is left subtree


# # 3. right of index at which preorder[0] is in at inorder is right subtree


# # recursively build tree at preorder [0] and left and right 

# # mid = 

# # 2 calls(preorder, inorder)










# # # left(prelist[1:mid+1],inorderlist[:mid])
# # # right(prelist,inorderlist)




# # # 2 facts
# # # 1. pre[0] is always the root
# # # 2. all values to left of root are in left subtree and 
# # #      all values to right of root are in right subtree


# # #          pre()
# # #          inorder()
# # # preorder traversal: 1,2,4,8,9,5,3,6,7
# # #                               5
# # # inorder traversal: 9,8,4,2,5,1,6,3,7
# # #                              5

# # # preorder traversal: 2,4,8,9, 5
# # #                           3

# # # inorder traversal: 9,8,4,2,5
# # #                          3

# # preorder traversal: 3,6,7, 11 ,12
# #                       1       
# # inorder traversal: 6,3,7,11,12
# #                      1       

# # preorder traversal: 6
# # inorder traversal: 6



# # preorder traversal: 7, 11 ,12
# # inorder traversal: 7,11,12
# #                    1       
# # preorder traversal: 11 ,12
# #                     0
# # inorder traversal: 11,12



# # preorder traversal:  12
# #                      0
# # inorder traversal: 12
# # 12

# # #                   1
# # #               2.      3 
# # #             4.  5.   6. 7
# # #            8
# # #          9. 10



# # # class TreeNode:
# # #     def __init__(val = 0,left = None,right = None):
# # #         self.val = val
# # #         self.left = left
# # #         self.right = right


# # class Solution:
# #     def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
# #         if not preorder or not inorder: return 
# #         mid = inorder.index(preorder[0])
# #         root = TreeNode(preorder[0])
# #         root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
# #         root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])



# #         return root









# #         if not preorder or not inorder: return
# #         mid = inorder.index(preorder[0])
# #         root = TreeNode(preorder[0])
# #         root.left = self.buildTree(preorder[1:mid+1],inorder[0:mid])
# #         root.right = self.buildTree(preorder[mid+1:],inorder[mid+1:])
# #         return root




# # #         3

# # #     9      20

# # #   1.    2   15    7
# # # 8

# # # 3 9  1 8 2 20 15 7 

# # # 8 1 9 2 3 15 20 7