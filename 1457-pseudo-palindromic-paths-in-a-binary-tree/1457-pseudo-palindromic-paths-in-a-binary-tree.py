# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        checkLis = []
        self.res = 0
        count = defaultdict(int)
        self.odd=0

        def backT(cur):
            if not cur: return 0
            count[cur.val]+=1
            oddChange = 1 if count[cur.val]%2==1 else -1
            self.odd+=oddChange

            if not cur.left and not cur.right:
                self.res += 1 if self.odd <=1 else 0
            backT(cur.left)
            backT(cur.right)  

            self.odd-=oddChange
            count[cur.val]-=1       



        backT(root)
        return self.res

        # def dfs(cur,path):
        #     if not cur: return
        #     path.append(cur.val)
        #     if not cur.left and not cur.right:
        #         checkLis.append(path[:])
        #         return
                
        #     dfs(cur.left,path[:])
        #     dfs(cur.right,path[:])
        #     # path.pop()
        # res =0




        # dfs(root,[])
        # for i in checkLis:
        #     cnt = Counter(i)
        #     mxV = 2
        #     correct = True
        #     # print(i)
        #     # print(cnt)
        #     for k,v in cnt.items():
        #         # print(k,v)
        #         if v%2==1: 
        #             mxV-=1
        #         if mxV <= 0:
        #             correct = False
                    
        #     if correct:
        #         res+=1
        # return res
        # print(checkLis)
        # def checkPal(lis):
        #     r = len(lis)-1
        #     for i in range(len(lis)//2):
        #         if lis[i] != lis[r]: return False
        #         r-=1
        #     return True

        # allPerms = []
        # allPermsA = []
        # def backtrack(lis, idx,choices, path):
        #     if idx >= len(lis):
        #         allPerms.append(path[:])

        #     for i,v in enumerate(lis):
        #         if i in choices:
        #             continue
                
        #         path.append(v)
        #         choices.add(i)
        #         backtrack(lis, idx+1, choices, path)
        #         choices.discard(i)
        #         path.pop()



        # for i in checkLis:
        #     allPerms = []
        #     backtrack(i,0,set(),[])
        #     allPermsA.append(allPerms[:])
        # res = 0
        # for i in allPermsA:
        #     for j in i:
        #         if checkPal(j):
        #             res+=1
        #             break
        # return res

        #             # append all these paths to checkLis


        # # call checkPal for all of these permutatiosn


        # # permutations
        # # 2,3,4
            
        # #     ø
        # #   2     3     4
        # #  3 4   2 4    
        # #  tmpLis = perm[:]
         
        # #     if i>= 

        # #     .remove(3)
        # #     choices 
        # #     if i[choices = 0: continue]

        # #          2 
        # #         3  4
        # #       4