class MedianFinder:

    def __init__(self):
        self.minNums =[]
        self.maxNums =[]
        # heapq.heapify(self.minHeap)
        # heapq.heapify(self.maxHeap)
#o(log(n))
    def addNum(self, num: int) -> None:
        # self.lis.append(num)
        heapq.heappush(self.minNums,-num)
        # print(self.minNums,self.maxNums)
        while self.minNums and self.maxNums and -self.minNums[0] > self.maxNums[0]:
            val = heapq.heappop(self.minNums)
            heapq.heappush(self.maxNums,-val)
        while len(self.minNums) - len(self.maxNums) >1:
            val = heapq.heappop(self.minNums)
            heapq.heappush(self.maxNums,-val)

        while len(self.maxNums) -len(self.minNums) >=1:
            val = heapq.heappop(self.maxNums)
            heapq.heappush(self.minNums,-val)


        # print(self.minNums,self.maxNums)

# 2 3 4


# 2 3 4
  
# -2 -4     3



        # 3 4

        # heapq.heappush(self.minHeap, num)
        # heapq.heappush(self.maxHeap, -num)
# O(1) + O(log(n) * (1/n))
    def findMedian(self) -> float:
        n = len(self.minNums)+ len(self.maxNums)
        return -self.minNums[0] if (n&1) else (-self.minNums[0] + self.maxNums[0])/2






        # self.lis.sort()
        # n=len(self.lis)
        # # return self.lis[n//2] if (n&1) else (self.lis[n//2] + self.lis[(n//2) -1]) /2



#         print(self.minHeap, self.maxHeap)
        
#         if len(self.minHeap)%2==0:
#             return (-(self.maxHeap[0]) + (self.minHeap[0]) )/ 2
#         if len(self.minHeap)==1: return self.minHeap[0]
#         tmp = self.minHeap[:]
# # [1,2,3]
# # 1
#         for i in range(len(self.minHeap)//2):
#             heapq.heappop(tmp)
#         return tmp[0]

        


# # # Your MedianFinder object will be instantiated and called as such:
# # # obj = MedianFinder()
# # # obj.addNum(num)
# # # param_2 = obj.findMedian()





# # 1 2 3 

# # sort then  nlogn

# # if length odd then return middle 












# # # 2 heaps 
# # # minheap  (large one):  [4,7]
 
# # # maxheap (small one):  [-2 -3]
# # # .add 2
# # # .add 3
# # # .add 7
# # # .add 4
# # # find Med I was



# # # check 1 length minheap greater than maxheap by 1 if so pop  from minheap and add that val to maxheap
# # #         and vice versa for case 1.5
# # check 2 if minheap[0] < maxheap[0]: pop from both and add to other heap
# #         and viceversa for case 2.5
# # case 3 find Med: O(1) if both lengths add together is even then add both of the root nodes of the heaps and then add them together and then divide by two. And the other case when the lengths are odd, we could just check which length is greater and then we were just return the head/root node.

# class MedianFinder:








    
#     def __init__(self):
#         self.smallHeap = [] # maxheap
#         self.largeHeap = [] # minheap
#     def addNum(self, num: int) -> None:
#         heapq.heappush(self.smallHeap, -num)
#         if (len(self.smallHeap) - len(self.largeHeap)) > 1:
#             val = heapq.heappop(self.smallHeap)
#             heapq.heappush(self.largeHeap, -val)
#         elif (len(self.largeHeap) - len(self.smallHeap)) > 1:
#             val = heapq.heappop(self.largeHeap)
#             heapq.heappush(self.smallHeap, -val)
#         if self.smallHeap and self.largeHeap and -self.smallHeap[0] > self.largeHeap[0]:
#             val = heapq.heappop(self.largeHeap)
#             val1 = heapq.heappop(self.smallHeap)
#             heapq.heappush(self.smallHeap, -val)
#             heapq.heappush(self.largeHeap, -val1)

#     def findMedian(self) -> float:
#         if (len(self.smallHeap) + len(self.largeHeap)) % 2== 0:
#             return (-self.smallHeap[0] + self.largeHeap[0]) /2
#         return -self.smallHeap[0]

#         # if (len(self.largeHeap) > len(self.smallHeap)):
#         #     return self.largeHeap[0]
# # Your MedianFinder object will be instantiated and called as such:
# # obj = MedianFinder()
# # obj.addNum(num)
# # param_2 = obj.findMedian()


# 6  10 2