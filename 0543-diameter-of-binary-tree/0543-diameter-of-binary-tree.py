# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        root.left,root.right
        root.left,root.left
        """
        # res = 0 
        # def calcDepth(root):
        #     if not root: return 0
        #     return 1 + max(calcDepth(root.left), calcDepth(root.right))

        '''
        
        '''
        self.res = 0
        def dfs(curr):
            if not curr: 
                return 0

            left = dfs(curr.left)
            right = dfs(curr.right)
            self.res = max (self.res, left + right)
            return 1 + max(left,right)
        dfs(root)
        return self.res

        # def dfs(r):
        #     dfs(r.left)
        #     dfs(r.right)
        #     return 1 + 


        # #set vars
        # nodeList, nodeDict = [], defaultdict(list)
        # #dfs
        # def dfs(node, nodeList, nodeDict):
        #     if not node:
        #         return
        #     nodeList.append(node.val)
        #     if not node.left and not node.right:
        #         nodeDict[id(node)].append(nodeList.copy())
        #     else:
        #         if node.left:
        #             dfs(node.left, nodeList, nodeDict)
        #         if node.right:
        #             dfs(node.right, nodeList, nodeDict)
        #     nodeList.pop()
        # #calc depth
        # def calcDepth(root):
        #     if not root: return 0
        #     return 1 + max(calcDepth(root.left), calcDepth(root.right))
        # maxLength = calcDepth(root) - 1
        # #call
        # dfs(root,nodeList,nodeDict)
        # #iter through values, see if max larger than current length from point a to b
        # output = list(nodeDict.values())
        # print(nodeDict.values())
        # print(output)
        # for i in range(len(output)):
        #     for j in range(len(output[i])):
        #         first, innerCount = 0, 0 
        #         for k in range(i+1, len(output)):
        #             if j >= len(output[k]): break
        #             if output[i][j] != output[k][j]: 
        #                 if(first == 0): 
        #                     first += 1
        #                     innerCount +=2
        #                 else: 
        #                     innerCount +=1
        #         maxLength = max(maxLength, innerCount)
        # return maxLength
