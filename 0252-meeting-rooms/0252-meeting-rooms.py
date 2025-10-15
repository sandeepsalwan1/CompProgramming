class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) <= 1: return True
        intervals.sort()
        
        newInterval= intervals[0]
        for i,(a,b) in enumerate(intervals):
            if i ==0:
                continue
            
            if newInterval[1]> a and newInterval[0] <= b:
                # newInterval[1] = max(newInterval[1],b)
                return False
            else:
                newInterval = [a,b]
        return True


            # [1,10] [3,11]






























        # intervals.sort(key = lambda x: x[0])
        # lastEnd = float('-inf')
        # for start,end in intervals:
        #     if start < lastEnd: return False
        #     lastEnd= end
        # return True


# -------

#  --- 
#      --
 
# [[0,2],[5,10],[15,20]]

# 10

# 15 < 10 : return false


# [0,2] old


# ,[1,10] new 


# if new[1] > old[0] and new[0] < old[1]: then theres overlap


# if new[1] > old[0] and new[0] < old[1]: then theres overlap


# # edge case what if start = end? 