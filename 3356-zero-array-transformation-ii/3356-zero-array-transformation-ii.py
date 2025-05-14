class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def possible(queries):
            diff = [0] * (len(nums)+1)
            for left, right, val in queries:
                diff[left] -= val
                diff[right+1] += val

            pref = [0] * len(nums)
            pref[0] = diff[0]
            for i in range(1, len(nums)):
                pref[i] = pref[i-1] + diff[i]

            for i in range(len(nums)):
                if nums[i] + pref[i] > 0:
                    return False
            return True

        if all(x == 0 for x in nums):
            return 0

        left, right = 0, len(queries) - 1
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if possible(queries[:mid+1]):
                ans = mid + 1
                right = mid - 1
            else:
                left = mid + 1
        return ans
