class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        res = 0
        diffList = []
        for firstVal, secondVal in costs:
            diffList.append(firstVal- secondVal)
        comparePrice = defaultdict(list)
        for i in range(len(diffList)):
            comparePrice[diffList[i]].append(costs[i])
        diffList.sort()
        print(diffList)
        print(comparePrice)
        
        for i in range(len(diffList)//2):
            extractedVal = comparePrice.get(diffList[i]).pop()
            print(extractedVal)
            res += int(extractedVal[0])
            print(res)
            
        for i in range(len(diffList)//2, len(diffList)):
            extractedVal = comparePrice.get(diffList[i]).pop() 
            res += int(extractedVal[1])
            
        return res