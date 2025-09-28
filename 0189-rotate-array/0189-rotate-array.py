# [1,2,3,4,5,6,7]

# l      r
# tmp,tmp3  = nums[r], nums[l]
# tmp2 = 0
# if r+1 < len(nums): 
#     tmp2 = nums[r+1]
#     nums[r] = nums[r+1]
# else:
#     r = 0

# nums[l] 


print(0%5)

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res = [0] * len(nums)
        for i in range(len(nums)):
            res[(i+k)%len(nums)] = nums[i]
        nums[:]=res

        # k%= len(nums)
        # res = 
        # nums[:] = nums[-k:] + nums[:-k] 







        # k%= len(nums)
        # nums[:] = nums[-k:] + nums[:-k]
        # if k==0: return nums
        # print(nums[len(nums)-k:len(nums)], nums[:len(nums)-k])
        # print(nums)
        # nums = (nums[len(nums)-k:len(nums)] + nums[:len(nums)-k])
        # print(nums)

        # return nums
        # # return nums[len(nums)-k:len(nums)] + nums[:len(nums)-k]






        # # k %= len(nums)
        # nums[:] = nums[-k:] + nums[:-k]
        #         # addThis = nums[:k+1]
        # # nums.extend(addThis)
        # # nums = (nums[k:])

        