class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        # dp = []
        @cache
        def recursive(i,j):

            if i >= len(word1): return len(word2) - j
            if j >= len(word2): return len(word1) - i
            if word1[i] == word2[j]:
                return recursive(i+1,j+1)

            return 1 + min(recursive(i,j+1),recursive(i+1,j), recursive(i+1,j+1))

        return recursive(0,0)
