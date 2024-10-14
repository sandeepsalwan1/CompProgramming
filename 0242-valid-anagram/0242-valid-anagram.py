class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
        input1, input2 = defaultdict(list), defaultdict(list)

        for i in s:
            input1[i] = input1.get(char) + 1
        for i in t:
            input2[i] = input2.get(char) + 1
        return input1 == input2

        # if len(s) != len(t): return False
        # # input1, input2 = set(), set()
        # n = len(s) // 2
        # b = len(s) - 1
        # for i in range(n):
        #     # input1.add(s[i])
        #     # input2.add(s[b])
        #     print(s[i])
        #     print(t[b])

        #     if s[i] != t[b]: return False
        #     b-=1
        # return True

