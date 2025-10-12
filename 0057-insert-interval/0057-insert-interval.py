# # # # '
# # # oldInter [[1,1],[3,5],[6,7],[8,10],[12,16]].     new In [3,10]  

# # # res 
# # # [[1,1], [3,10], ...]


# # # #         2 8
# # # #           end is     


# # # [[1,3],[6,9]], newInterval = [2,5]





# # # [4,5]

# # # if 

# # #  unpack this 2d list
# # # case 1: if either first or second newInterval greater than first interval of the 2d list  and less than second element in 2d list then
# # # if one 
# # # min(first2d, currel) 
# # # max(second2d, curr2ndel) 
# # #     case1: if curr2ndel > 2d2ndel go to next one keep going until 8<= 2d2ndel
# # #                 if 8 >= 2dnfirst new end = 2dnsecond 
# # #                 new start = start 
# # #                 new End = 

# # # case 2: insert at currentindex '
# # '




# # [[1,3], [6,9]]



# # [[1,3], [6,9]]



# # [[1,2],[3,5],[6,7],[8,10],[12,16]]

# # [[1,2],[3,5],[6,7],[8,10],[12,16]]

# # res: [[1,2], [3,10],


# # newInterval = [3,10]
# # newInterval[0] = min( new[0], old[0])
# # newInterval[1] = max( new[1], old[1])



# # check last index of new Index if less than then 
# #     add as is and add as is 

# # if first index newInterval greater the first index oldInterval: 
# #     append the current element to res. 





# # newIndex [0,0],


# # newIndex [2,5],


# fit in interval


# can either add start or end



# iterate through and then check both 


# when old[1]> new[0] and old[0] > new[1]

# 1,3 


# add new interval 

# prev = 0





# for i in intervals:


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # insert then merge
        if not intervals: return [newInterval]
        idx =0
        for i,(a,b) in enumerate(intervals):
            if a< newInterval[0]:
                idx= i+1
        print(idx)
        intervals.insert(idx,newInterval)
        print(intervals)
        res = []
        newInt = intervals[0]
        for i,(a,b) in enumerate(intervals):
            if i==0:continue
            if newInt[0]<= b and newInt[1] >= a:
                newInt[0]= min(newInt[0], a)
                newInt[1]= max(newInt[1], b)
            else:
                res.append(newInt)
                newInt = [a,b]
        res.append(newInt)

        return res
        # 1




























        # res = []
        # prev = float('inf')
        # for i,(x,y) in enumerate(intervals):
        #     if newInterval[0] <= x:
        #         prev = i
        #         break
        # if prev == float('inf'): intervals.append(newInterval)
        # else: intervals.insert(prev, newInterval)
        # res =[]
        # newIn= []
        # for i,(x,y) in enumerate(intervals):
        #     if i == 0: 
        #         newIn = [x,y]
        #         continue
        #     if x <= newIn[1] and y >= newIn[0]:
        #         newIn[1] = max(y,newIn[1])
        #     else:
        #         res.append(newIn)
        #         newIn = [x,y]
            
        # res.append(newIn)
        # return res


newIn = [1,10]

[1,10]

[[1, 2], [3, 5], [4, 8], [6, 7], [8, 10], [12, 16]]


































        # res = []
        # for i in range(len(intervals)):
        #     if newInterval[1] < intervals[i][0]:
        #         res.append(newInterval)
        #         return res + intervals[i:]
        #     elif newInterval[0] > intervals[i][1]:
        #         res.append(intervals[i])
        #     else:
        #         newInterval[0] = min( newInterval[0], intervals[i][0])
        #         newInterval[1] = max( newInterval[1], intervals[i][1])

        # res.append(newInterval)
        # return res



















        # res = []
        # for i in range(len(intervals)):
        #     if newInterval[1] < intervals[i][0]:
        #         res.append(newInterval)
        #         return res + intervals[i:]
        #     elif newInterval[0] > intervals[i][1]:
        #         res.append(intervals[i])
        #     else:
        #         newInterval  = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        


        # res.append(newInterval)
        # return res





        # res = []
        
    
        # for i in range(len(intervals)):
        #     if newInterval[1] < intervals[i][0]:
        #         res.append(newInterval)
        #         return res
        #         # intervals.insert(i, newInterval)
        # for i in range(len(intervals) - 1):
        #     start = None
        #     while intervals[i][1] >= intervals[i+1][0] and intervals[i][0] <= intervals[i+1][1]:
        #         start = min(newInterval[0],intervals[i][0])
        #         end = max(newInterval[1],intervals[i][1])
        #         i+=1
        #     print(intervals[0])
        #     if start: res.append([start,end])
        #     elif i <len(intervals): res.append(intervals[i])
        # print(res)