# '
# [[1,1],[3,5],[6,7],[8,10],[12,16]]. [4,8]
#         2 8
#           end is     


# [[1,3],[6,9]], newInterval = [2,5]

# [4,5]

# if 

#  unpack this 2d list
# case 1: if either first or second newInterval greater than first interval of the 2d list  and less than second element in 2d list then
# if one 
# min(first2d, currel) 
# max(second2d, curr2ndel) 
#     case1: if curr2ndel > 2d2ndel go to next one keep going until 8<= 2d2ndel
#                 if 8 >= 2dnfirst new end = 2dnsecond 
#                 new start = start 
#                 new End = 

# case 2: insert at currentindex '


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        
    
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                intervals.insert(i, newInterval)
        res = []
        for i in range(len(intervals) - 1):
            start = None
            while intervals[i][1] >= intervals[i+1][0] and intervals[i][0] <= intervals[i+1][1]:
                start = min(newInterval[0],intervals[i][0])
                end = max(newInterval[1],intervals[i][1])
                i+=1
            print(intervals[0])
            if start: res.append([start,end])
            elif i <len(intervals): res.append(intervals[i])
        print(res)
        while i < len(intervals) -1:
            start = intervals[i][0]
            if intervals[i][1] > intervals[i+1][0]: 
                newEnd = intervals[i+1][1]
            i+=1
            res.append([start,end])
        print(res)
        # start = 
        return intervals