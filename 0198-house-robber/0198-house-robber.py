class Solution:
    def rob(self, nums: List[int]) -> int:
        nums.append(0)
        rob1,rob2 = 0,0
        for i in range (len(nums) -3, -1,-1):
            nums[i] = max(nums[i+1],nums[i]+ nums[i+2])
        return max(nums[0],nums[1])
        # for n in nums:
        #     temp = max(n+rob1,rob2)
        #     rob1 = rob2
        #     rob2 = n 
        # # 1 23 1 
        # # 1 2 3 1 1000 5 2
        # #rob1, rob2 = 0,1 

        # return max(nums[0] + self.rob(nums[2:]), self.rob(nums[1:]))
