class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # perms = [[]]
        # res = []
        # for n in nums:
        #     subset = []
        #     for p in perms:
        #         for i in range(len(perms) + 1):
        #             subsetCopy = p.copy()
        #             subsetCopy.insert(i,n)
        #             res.append(subset.copy)
        #     perms.append(subset)

        # # [] 3  32 23   132  312 321.      123 213 231
        # return res
       
        if len(nums) == 0: return [[]]
        perms = self.permute(nums[1:])
        res = []
        # for n in nums:
        #     subset = []
        for p in perms:
            for i in range(len(p) + 1):
                subsetCopy = p.copy()
                subsetCopy.insert(i,nums[0])
                res.append(subsetCopy)
        return res


        # [] 3  32 23   132  312 321.      123 213 231
        # return res
                    