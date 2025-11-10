class Solution:
    def expand(self, s: str) -> List[str]:
        letDict = defaultdict(list)
        start = False
        idx = 0
        for i in s:
            if i == "{":
                start = True
            elif i == "}":
                start = False
                # letDict[idx].append(set())
                idx +=1
            elif start:
                if i.isalpha():
                    letDict[idx].append(i)
            elif i.isalpha():
                letDict[idx].append(i)
                idx +=1
        print(letDict)
        va = list(letDict.values())
        print(va,"v")
        res = []
        def backtrack(cur, i):
            if i >= len(va):
                res.append("".join(cur))
                print(i)
                return
            
            print(cur,i)
            for c in va[i]:
                # if len(va[i]) ==1:
                #     cur.append(c)
                #     backtrack(cur, i+1)
                #     cur.pop()

                #     break

                
                cur.append(c)
                backtrack(cur, i+1)
                cur.pop()

        backtrack([],0)
        res.sort()
        return res
        # if doubleCount ==doubleCountMax: break
        # doubleCountMax = len(letDict)
        # doubleCount=0

                    

            # res.append("".join(cur))

            # [[a,b],[c],[d,e],[f]]

#             a b
#            c    c
#          d. e   d e
#         f  f    f  f
#  i > len(va): 
#  appendr
#  return
#  for c in va[i]:
#     append(c)
#     back(i+1)
#     pop()


#         0:[a,b]
#         1:[c]
#         2:[d,e]
#         3:[f]
     


# res = []


#         {a,b}


#         {}

#     #  {

#     # start 
    