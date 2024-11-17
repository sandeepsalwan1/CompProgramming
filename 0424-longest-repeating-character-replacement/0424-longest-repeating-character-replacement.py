class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s: return 0
        res = 1
        for c in range(len(s)):
            newDict = {}
            newDict[s[c]] = newDict.get(s[c],0) + 1
            for r in range(c+1, len(s)):
                newDict[s[r]] = newDict.get(s[r],0) + 1
                input = list(newDict.values())
                print(input)
                input.sort(reverse = True)
                if(len(input) > 1 and (sum(input)-input[0]) > k): 
                    break
                inputVal = sum(input)
                res = max(res, inputVal)
        return res