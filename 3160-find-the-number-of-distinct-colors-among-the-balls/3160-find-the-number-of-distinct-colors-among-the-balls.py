'''
        #hashmap with key from 0->limit+1 and value = color. 
        #count variable
        #default dict 
                
        resList
        for every query check if val = 0  
          if val != 0 resCounter+=1 
          add resCounter to 

          '''

# [[1,4],[2,5],[1,3],[3,4]]

# resCounter   2 
# resList
# hash. 1:4 

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        resCounter, resList, hashColor = 0, [], defaultdict(int)
        hashAdded = defaultdict(list)
        for first,second in queries:
            if hashColor[first] != 0: 
                hashAdded[hashColor[first]].remove(first)
                if len(hashAdded[hashColor[first]]) == 0: del hashAdded[hashColor[first]]

            hashColor[first] = second
            hashAdded[second].append(first)
            resCounter = len(hashAdded)
            resList.append(resCounter)
        return resList
            #make sure its different
            #hashColor[first] != 0 and  count is now 1 then add 
            #add if first   query val not unique
        #     hashColor[first] = second
        #     for i in hashAdded.values():

        #     if second not in hashColor.values(): 
        #         resCounter +=1  
        #     if hashColor[first] == 0:
        #         hashAdded[second] = hashAdded[second] + 1
        #     else: 
        #         hashAdded

        #     hashColor[first] = second

        #     resList.append(resCounter)
        # return resList