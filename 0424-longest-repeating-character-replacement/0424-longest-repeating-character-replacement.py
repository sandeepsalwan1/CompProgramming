class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l,r=0,0
        currDict = {}
        while r < len(s):
            currDict[s[r]] = currDict.get(s[r],0 ) + 1
            while ((r-l +1 )- max(currDict.values() ) > k) and l < len(s):
                currDict[s[l]] = currDict.get(s[l],0 ) - 1
                l+=1
            res = max(res, r-l+1)
            r+=1
        return res


                # for c in range(len(s)):
        #     newDict = {}
        #     newDict[s[c]] = newDict.get(s[c],0) + 1
        #     for r in range(c+1, len(s)):
        #         newDict[s[r]] = newDict.get(s[r],0) + 1
        #         input = list(newDict.values())
        #         input.sort(reverse = True)
        #         if(len(input) > 1 and (sum(input)-input[0]) > k): 
        #             break
        #         inputVal = sum(input)
        #         res = max(res, inputVal)


                # for c in range(len(s)):
        #     newDict = {}
        #     newDict[s[c]] = newDict.get(s[c],0) + 1
        #     for r in range(c+1, len(s)):
        #         newDict[s[r]] = newDict.get(s[r],0) + 1
        #         input = list(newDict.values())
        #         input.sort(reverse = True)
        #         if(len(input) > 1 and (sum(input)-input[0]) > k): 
        #             break
        #         inputVal = sum(input)
        #         res = max(res, inputVal)