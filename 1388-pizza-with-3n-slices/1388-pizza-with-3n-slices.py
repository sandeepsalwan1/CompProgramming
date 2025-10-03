class Solution:
    def maxSizeSlices(self, A):
        @cache
        def dp(i, j, k, cycle=0):
            if k == 0: return 0
            if j - i + 1 < k * 2 - 1: return -inf
            return max(dp(i + cycle, j - 2, k - 1) + A[j], dp(i, j - 1, k))
        return dp(0, len(A) - 1, len(A) // 3, 1)