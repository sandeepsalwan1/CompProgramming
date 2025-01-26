class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        res = [0] * numberOfUsers
        messageEvents = []
        offlineHash = defaultdict(list)
        for first,second,third in events:
            if first == "OFFLINE":
                offlineHash[int(third)].append(int(second))
            else:
                messageEvents.append([first,second,third])
        for first,second,third in messageEvents:
            second = int(second)
            if third == "ALL":
                for idx in range(numberOfUsers):
                    res[idx] +=1 
            elif third == "HERE":
                for idx in range(numberOfUsers):
                    # if (idx not in hash or all(second <= x or second < x+60 for x in range hash[idx])):
                    offlineList = offlineHash[idx]
                    isOnline = True
                    for iSecond in offlineList:
                        if iSecond <= second < iSecond+60:
                            isOnline = False
                            break
                    if isOnline:
                        res[idx] +=1 
            else:
                listComp = [int(x[2:]) for x in third.split(" ")]
                for idx in listComp:
                    res[idx] +=1           

        return res
