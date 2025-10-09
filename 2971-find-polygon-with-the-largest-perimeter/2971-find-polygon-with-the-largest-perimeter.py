class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        cur = 0
        cnt =0
        res = -1
        total = 0
        # if len(nums) == 3 and nums[-1] >= nums[0]+nums[1]: return -1
        for i in nums:
            if total > i: res = total +i
            total +=i
        return res

        #     if cnt >=3: 
        #         if i >= cur: break
        #     cur+=i
        #     cnt+=1

        # return cur 


# 1 1 2


# 1 1 
# total > num