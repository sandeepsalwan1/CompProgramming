# you can have multiple pointers. 

# r
# O(n)

# O(1)

# ""

# ["",""]


# ["flower","flow","flight"]

# res ="flower"

# flow","flight"]
# 0        2

# flow



class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]
        for i in range(1,len(strs)):
            p = 0
            for j in range(len(res)):
                if p >= len(strs[i]) or strs[i][p] != res[j]:
                    res = res[:j] 
                    break
                p+=1
        
        return res


        return res

