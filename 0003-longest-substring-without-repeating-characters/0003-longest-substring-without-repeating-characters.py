'''
brute: double for loop look through every substring on^2


optimal: sliding window keep adding l until valid 

        b    b   b             bb
                
        b 

        a   b   c   a   b   c   b   b
            l,          r

            while loop and check 
            2 pointer


           p    w   w   k   e   w
           lr                    
            set = (w,k,e)

            res = 3
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <=1: return len(s)

        seen = set()
        l,r=0,0
        res =0
        while r< len(s):
            while s[r] in seen:
                seen.discard(s[l])
                l+=1
            seen.add(s[r])
            res = max(res,r-l+1)
            r+=1
        return res







        checkSet = set()
        n = len(s)
        res = 0
        l,r = 0,0
        while r < n:
            if s[r] not in checkSet: 
                checkSet.add(s[r])
                res = max(res, r-l+1)
                r+=1
            else:
                checkSet.remove(s[l])
                l+=1

        return res

    # time: O(n)
    # set 


# bbbbb




        # checkSet = set()
        # res = 0
        # l,r = 0,0
        # while r < len(s):
        #     if s[r] not in checkSet:
        #         res = max(res, r-l+1)
        #         checkSet.add(s[r])
        #         r+=1
        #     else: 
        #         checkSet.remove(s[l])
        #         l+=1
        # return res
