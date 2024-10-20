class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counter = defaultdict(list)
        # dictionary  [[a:1b:2]] :[bab][baa]
        res = defaultdict(list)
        for i in strs:
            count = [0] * 26
            for j in i:
                count[ord(j) - ord("a")] += 1
            res[tuple(count)].append(i)
        
        return (list(res.values()))

        firstSet = set()
        for i in range(len(strs)): 
            firstAdd = Counter(strs[i])
            if(firstAdd in firstSet): continue
            firstSet.add(firstAdd)
            resAdd = [strs[i]]
            for j in range(i+1,len(strs)):
                secondAdd = Counter(strs[j])
                if(secondAdd == firstAdd):
                    resAdd.append(strs[j])
            res.append(resAdd)

            # setInput.add(Counter(i))
            # res.a
            # input[(Counter(i))].append([i])
        # for j in input:
            # res.append(input[j]) 
        return res


# 