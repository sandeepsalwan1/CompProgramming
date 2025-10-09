class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        
        # Calculate prefix sums for efficient sum calculation
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        
        max_perimeter = -1
        
        # Try to form polygons starting from smallest possible (3 sides)
        # Check each position as potential longest side
        for i in range(2, n):  # i is the index of the longest side
            # Sum of all sides except the longest (nums[i])
            sum_of_others = prefix_sum[i]
            
            # Check polygon inequality: sum of other sides > longest side
            if sum_of_others > nums[i]:
                # Valid polygon found, calculate perimeter
                perimeter = sum_of_others + nums[i]
                max_perimeter = perimeter  # Keep updating as we go (larger perimeters come later)
        
        return max_perimeter
    #     nums.sort()
    #     cur = 0
    #     cnt =0
    #     if len(nums) == 3 and nums[-1] >= nums[0]+nums[1]: return -1
    #     for i in nums:
    #         if cnt >=3: 
    #             if i >= cur: break
    #         cur+=i
    #         cnt+=1

    #     return cur 

    # Sort the array in ascending order
  