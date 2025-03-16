class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        l,r = 1,max(ranks)* cars**2
        res = float('inf')
        while r >= l:
            mid = (r+l)//2
            sumVal = 0
            for i in ranks:
                sumVal += floor((mid/i)**0.5)
            if sumVal >= cars:
                res = mid 
                r = mid-1
            else: l = mid+1
        return res

# [4,2,3,1]

# 16

# 16/4
# 16/3
# 16/1 **0.5
# 4
# 2+ 2 + 2 + 4

#         #sort 
#         # test every combination where the 4 mechs equal to 10 cars
#         # ranks.sort()
        
#         # def backtracking()

# (minutes)

# r * n^2 = time


# n = (time/r)**0.5


# [1,max(ranks)* cars**2]

# iterate through rank and divide by current rank to get n(or number of cars)
# add that to variable sumVal 

# if sumVal > mid res = mid r = m-1
# else l = m+1
# let  n = len(ranks)
# n* log max(ranks)* cars**2

# halving arr every iteration
# SC: O(1)
        