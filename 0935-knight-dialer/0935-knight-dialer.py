class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10

        mod = 10**9 + 7
        jumps = [1, 4, 2, 2]  # [D, A, B, C]

        for _ in range(n - 1):
            tmp = [0] * 4
            tmp[0] = jumps[3]
            tmp[1] = 2 * jumps[2] + 2 * jumps[3]
            tmp[2] = jumps[1]
            tmp[3] = 2 * jumps[0] + jumps[1]
            jumps = tmp

        return sum(jumps) % mod