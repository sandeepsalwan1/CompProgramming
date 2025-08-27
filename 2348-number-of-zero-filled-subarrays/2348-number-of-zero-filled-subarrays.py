class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        # zF = [0] * (len(nums))
        prev = 0
        res = 0
        for i,v in enumerate(nums):
            if v == 0:
                # if i ==0: prev =1; continue
                prev += 1
            else: prev = 0
            res += prev
        # res = 0
        # for i,v in enumerate(zF):
        #     res+= v
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