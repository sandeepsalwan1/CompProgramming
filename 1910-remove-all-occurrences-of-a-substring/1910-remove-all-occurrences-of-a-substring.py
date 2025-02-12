class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        res = []
        n = len(part)
        part2 = list(part)
        for i in s:
            res.append(i)
            if len(res) >= n and res[-n:] == part2:
                for i in range(n): res.pop()
        return ("").join(res)
