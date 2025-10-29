class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = 0
        curStr = ""
        #numbers guaranteed for the innput before open brack
        for i in s:
            if i.isdigit():
                num = num*10 +int(i)
            
            elif i == "[":
                stack.append([curStr, num])
                curStr, num = "", 0
            elif i == "]":
                prevString, numMult = stack.pop()
                curStr = prevString + curStr *numMult 
            else:
                curStr += i
        return curStr


#  stack - sim to valid parenthesis

#  recursive backtracking? inner to out? find mos tnested one
# stack [] 
# append at [  like if statement and pop ]??? sim to vlaid

# 3[a2[c]] 
#      i
# 3 
# ["",3, (a,), (c * 2)]
# [("", 3),  ("a",2) "c"]

           
    # "" + 3 * ( a + 2*"c")

# Str = c repeat cnt = 2
# 3 * acc
# accaccacc

# ab2[c]de
# a 
# b 
# str = ab
# num [(ab,2),(str =c)]
# ab + cc

# # str = d
# # str = e

# # abccde
# O(n) TC and SC 

