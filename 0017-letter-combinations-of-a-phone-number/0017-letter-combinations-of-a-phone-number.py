class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }   
        res = []
        def backtrack(idx, builder):
            if len(digits) <= idx:
                res.append("".join(builder))
                return
            number = digits[idx]
            for letter in letters[number]:
                builder.append(letter)
                backtrack(idx+1, builder)
                builder.pop()
        
        backtrack(0,[])
        return res








        # map the letters then backt
        # if not digits: return []
        # res = []
        # hashM = {2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}
        # print(hashM[2])
        # def backtrack(i, cur):
        #     if i>= len(digits): 
        #         res.append("".join(cur[:]))
        #         return
        #     print(digits[i])
        #     print(hashM)
        #     print(hashM[int(digits[i])])
        #     for j in range(len(hashM[int(digits[i])])):
        #         cur.append(hashM[int(digits[i])][j])
        #         backtrack(i+1,cur)
        #         cur.pop()
        # backtrack(0,[])
        # return res
        #             23
        # i      a     
        #       d  e 