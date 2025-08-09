class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # take from left or right 
        if len(s1)+len(s2)!= len(s3): return False
        # self.val = ""
        @cache
        def dp(l,li):
            if l + li >= len(s3): return True
            
            if l < len(s1) and s1[l] == s3[l+li] and dp(l+1,li): return True
            elif li < len(s2) and s2[li] == s3[l+li] and dp(l,li + 1): return True
            return False
        return dp(0,0)

#         aadbbcbcac

#         10

# 0,0 >= 1: True

# if l > len(s1) and s1[l]= s3[l+li]: 
#         s1 = a
#         s2 = ""
#         s3 = a