class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        # map it and then.i convert it 
        mapDict ={i:v for i,v in enumerate(mapping)}
        checkDict = {}
        newSort = nums.copy()
        # print(mapDict)
        for i,v in enumerate(nums):
            cur = 0
            for j in str(v):
                cur = cur*10 + mapDict[int(j)]
            # print(newSort)
            newSort[i]= [cur,i]
            # print(newSort)

            checkDict[(i,cur)] = v
        # print(newSort)
        newSort.sort()
        # print(newSort)
        # print(checkDict)
        for i, (v,y) in enumerate(newSort):
            # print(i,v,y)
            nums[i] = checkDict[(y, v)]
        return nums
            # newSort.append(v)