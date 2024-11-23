class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) -1 
        while r>= l:
            m = (l+r) //2
            # if nums[l] <= nums[r]: return max(res, nums[l])
            if nums[m] == target:return m
            #in left sorted 
            if nums[m] >= nums[l]:
                if target > nums[m] or target < nums[l]:
                    l=m+1
                else:
                    r= m -1
            #in right sorted
            elif nums[m] < nums[l]:
                if target < nums[m] or nums[r] < target:
                    r = m - 1
                else:
                    l = m +1
        return -1
                
    #             return self.binarySearch(nums[l:r+1])
    #     #         elif nums[m] >= target:
    #     #             if target < nums[l]:
    #     #                 r=m-1
    #     #             else:
    #     #                 l= m +1
    #     # return n-1
    #         # res = max(res,nums[m])
    #     return -1
    # def binarySearch(self, nums, target):
    #     l,r = 0, len(nums) -1 
    #     while r>= l:
    #         m = (l+r) //2
    #         if nums[m] == target:
    #             return m 
    #         if nums[m] >= nums[l]:
    #             l=m+1
    #         else: r= m -1
    #     return -1


    #     #     if(nums[m] == target) : return m

    #     # return -1


    #     #     2,1

    #     #     2 2 