class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        for i, num in enumerate(nums):
            if not stack or num < nums[stack[-1]]:
                stack.append(i)
        maxWidth = 0
        for j in reversed(range(len(nums))):
            while stack and nums[j] >= nums[stack[-1]]:
                maxWidth = max(maxWidth, j-stack[-1])
                stack.pop()
        return maxWidth