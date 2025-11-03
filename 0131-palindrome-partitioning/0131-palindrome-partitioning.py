#        f1                                     aabc
#         f2                            a.      aa           aab    aabc
#        f3                         a    ab     b    bc               
#       f4                        b                 
#      f5                                
#                                             aa       i= 1
#  i = 2
#                                             b bc
# i= 3
#                                             c 

#                                             why pop?


#                                             a,a 
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def checkPali(s):
            l,r = 0, len(s)-1
            while r> l:
                if s[r]!=s[l]:return False
                l,r = l+1,r-1
            return True
        res = []
        print(checkPali("aa"))

        def backT(cur, idx):
            if idx >= len(s):
                res.append(cur.copy())
                return 
            for j in range(idx,len(s)):
                if checkPali(s[idx:j+1]):
                    cur.append(s[idx:j+1])
                    backT(cur,j+1)
                    cur.pop()


        backT([],0)
        return res   
#   Input: s = "aab"

# cur = []
# for i in range(s):
# Output: [["a","a","b"],["aa","b"]]
#         test()

# Input: s = "aab"
            

  
# res = [[a, a ,b], ]


# [] 0


# +a [a] 1
#     +a [a, a] 1
    
#         +b [a, a,b] 1     res++
#         -b
    
#     ["ab"] XX for loop ends

#     -a

#     ["aa"] good [a, a] 2
#         +b [a, a] 3 res++
#         -b

    
# [aab not pal]

  

# +a [a] 1

# f1 
#    [a, a ,b] ([],0)

#     add a
#        i:
#      [a, a ,b] ([a],1)
#         [a, a ,b] ([a, a],2)
#             app
#             [a, a ,b] ([a, a, b],3) res adds this
#             pop
#         [a, a] ([a, a],2)

#     pop()
#     [aa], 2 


    




# i


# []
# #         res = []















# #     def checkPal(self,lis):
# #         r = len(lis)-1
# #         for l in range(len(lis)//2):
# #             if lis[l] != lis[r]: return False
# #             r-=1
# #         return True

# #     def partition(self, s: str) -> List[List[str]]:
# #         res = []
#         def backtracking(curr,i):
#             if i >= len(s): 
#                 res.append(curr[:])
#                 return
#             for j in range(i,len(s)):
#                 if self.checkPal(s[i:j+1]):
#                     curr.append(s[i:j+1])
#                     backtracking(curr,j+1)
#                     curr.pop()
#         backtracking([],0)
#         return res

# #           aabc
# #         a       aa.   aab.   aabc
# #        a ab      b. bc
# #       b          

















# #         r= len(lis)-1
# #         for l in range(len(lis)):
# #             if lis[l] != lis[r]: return False
# #             r-=1
# #         return True
# #     def partition(self, s: str) -> List[List[str]]:
# #         res = []
# #         def backtrack(cur,i):
# #             if i >= len(s):
# #                 res.append(cur[:])
# #                 return 
# #             for j in range(i,len(s)):
# #                 if self.checkPal(s[i:j+1]):
# #                     cur.append(s[i:j+1])
#                     backtrack(cur,j+1)
#                     cur.pop()

#         backtrack([],0)
#         return res

# #             if not self.checkPal(c):
# #                 return
# #             # check = [cur[:i+1] for i in range(len(cur))]   
# #             # cur+=(s[i])
# #             # backtrack(cur, i+1)
# #             # cur = cur[1:]
# #             # cur[-1] += s[i]
# #             # backtrack(cur, i+1)
# #             # cur[-1] -= s[i]
# # ,,,
# #         backtrack(s[0],0)
# #         return res
# #         #a
# #         # "aab"
# #         # for i 
# #         # for loop two pointer

# #         # second is start at current value and 2 pointer check if values at left and right are equal if so continue otherwies return 



# # # # n*2^n

# # # n. 



# # # 2^n

# # # aux space is constant