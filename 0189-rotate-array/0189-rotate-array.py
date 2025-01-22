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




class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]
                # addThis = nums[:k+1]
        # nums.extend(addThis)
        # nums = (nums[k:])

        