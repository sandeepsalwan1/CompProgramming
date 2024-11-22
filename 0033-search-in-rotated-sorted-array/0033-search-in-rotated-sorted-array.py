class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        pivot = l
        
        def binary_search(left: int, right: int) -> int:
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        result = binary_search(0, pivot - 1)
        if result != -1:
            return result
        
        return binary_search(pivot, len(nums) - 1)

# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         l,r = 0, len(nums) -1 
#         while r>= l:
#             m = (l+r) //2
#             # if nums[l] <= nums[r]: return max(res, nums[l])
#             if nums[m] == target:return m jj
#             if nums[m] >= nums[l]:
#                 if target < nums[l]:
#                     l=m+1
#                 else:
#                     r= m -1
#             elif nums[m] <= nums[l]:
#                 if target < nums[l]:
#                     l=m+1
#                 else:
#                     r= m -1
        
#             # res = max(res,nums[m])
#         return -1
#     def binarySearch(self, nums, target):
#         l,r = 0, len(nums) -1 
#         while r>= l:
#             m = (l+r) //2
#             if nums[m] == target:
#                 return m 
            
#             if nums[l] > nums[r]: 
#             if nums[l] <= nums[r]: return max(res, nums[l])
#             if nums[m] >= nums[l]:
#                 l=m+1
#             else: r= m -1
#             res = max(res,nums[m])
#         return res
#             if(nums[m] == target) : return m
#         return -1


#         #     if(nums[m] == target) : return m

#         # return -1


#         #     2,1

#         #     2 2 