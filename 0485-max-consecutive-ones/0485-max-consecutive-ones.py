class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxV = 0
        count =0
        for i in nums:
            if i == 1:
                count+=1
                maxV = max(count,maxV)
            else: count = 0
        return maxV