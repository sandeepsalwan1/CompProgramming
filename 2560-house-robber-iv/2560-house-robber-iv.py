# 5
# number of houses <= 5

# 2,3,5


# 9

# # if i <= len(nums): return 0 
# # return max(take(i+2) + nums[i], take(i+1))

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        l,r = 1, max(nums)
        res = float('inf')
        while r >= l:
            mid = (r+l)//2
            count = 0
            i = 0
            while i < len(nums):
                if nums[i] <= mid:
                    count +=1
                    i+=2
                else: i+=1
                if count == k: break
            if count == k:
                res = mid
                r = mid -1
            else:
                l = mid +1
        return res




            