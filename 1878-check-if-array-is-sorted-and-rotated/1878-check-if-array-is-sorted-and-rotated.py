'''
        #o n ^2 is to make a list starting at point in arr e.g [1:n] and [0:1] to new list and check if sorted for every element. 
2 1 3 4
l   r



        3 4 5 1 2 
            l r

            if nums[r] > nums[l] return false 
        return true
       prev = 3 if greater than 3 
              1 2 3 4 5 
[2,1,3,4]'''

class Solution:
    def check(self, nums: List[int]) -> bool:
        l,r = 0,1
        maxVal= nums[0]
        first = 0 
        while r < len(nums):
            # if first == 0 and nums[r] >= nums[l]:
                # l = r
            if first == 0 and nums[r] < nums[l]:
                first +=1
                maxVal = nums[l]
            
            elif first == 1 and (nums[r] < nums[l] or nums[r] > maxVal):
                return False
            r+=1
            l+=1

        # 7 1 5
        return nums[0] >= nums[-1] if first ==1 else True
        # return True