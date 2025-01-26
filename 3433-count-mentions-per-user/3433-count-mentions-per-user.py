from collections import defaultdict

class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:

        # first make a dictionary containg times when each id is offline
        # we can use this to check against the times when a here message is sent

        offline = defaultdict(list)

        for e in range(len(events)):
            if events[e][0] == "OFFLINE":
                offline[int(events[e][2])].append(int(events[e][1]))

        messages = [0]*numberOfUsers

        for e in range(len(events)):

            mentions_string = events[e][2]
            timestamp = int(events[e][1])
            
            if events[e][0] == "MESSAGE":

                if mentions_string == "ALL":
                    messages = [x+1 for x in messages]

                elif mentions_string == "HERE":
                    for user in range(numberOfUsers):
                        if user not in offline.keys() or all([timestamp < offline[user][x] or timestamp >= int(offline[user][x]) + 60 for x in range(len(offline[user]))]):
                            messages[user] +=1
                else:
                    user_list = [int(x[2:]) for x in mentions_string.split(" ")]
                    for user in user_list:
                        messages[user] += 1

        return messages