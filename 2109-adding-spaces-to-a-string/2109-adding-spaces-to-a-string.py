class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
    # spaces.sort()
    # spacesR = [i-1 for i in spaces]
        res = []
        # i,j =0,0
        # while i < len(s) and j < len(spaces):
        #     if i < len(s)
        # print(spaces)
        spaceIdx = 0
        for i in range(len(s)+1):
            if spaceIdx < len(spaces) and spaces[spaceIdx] ==i:
                res.append(" ")
                spaceIdx+=1
                # continue
            if i== len(s):continue
            res.append(s[i])

            # if s[i]
            # spa
        return "".join(res)