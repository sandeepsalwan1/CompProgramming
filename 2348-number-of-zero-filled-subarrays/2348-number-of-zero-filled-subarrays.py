class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        zF = [0] * (len(nums))
        for i,v in enumerate(nums):
            if v == 0:
                if i ==0: zF[i] =1; continue
                zF[i] = zF[i-1] + 1
        res = 0
        for i,v in enumerate(zF):
            res+= v
        return res
        # [0] 

        # 2^0 + 1
        # [00]
        # 2^1 + 1
        # 0 0 0 

        # 3 choose 3 

        # 1 

        # 3 choose 2
        # = 2

        # 3 choose 1 = 3