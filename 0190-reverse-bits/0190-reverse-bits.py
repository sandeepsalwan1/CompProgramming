class Solution:
    def reverseBits(self, n: int) -> int:
        # 32 bits
        # you want to swap 1st bit with 31st(leftmost)

        # 00000001101

        # 10110000
        start,po = 0,31
        while n:
            start += (n&1)<< po
            n = n>>1
            po-=1
        return start
        # output = str(n)
        print(n)
        # reversed
        # print(output)