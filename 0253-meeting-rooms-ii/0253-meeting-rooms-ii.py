class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # events.sort()

        events = []
        for i,b in intervals:
            events.append([i,1])
            events.append([b,-1])
        events.sort()
        res = 0
        cnt = 0
        for t,d in events:
            if d == 1:
                cnt +=1
                res = max(cnt, res)
            else:
                cnt -=1

        return res



 