class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        numStr = [str(i) for i in nums]
        numStr.sort(key = lambda x: x *10, reverse=True)
        if numStr[0] == "0": return "0"
        return "".join(numStr)
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
        # hash = {}
        # print(nums)

        # for i in nums:
        #     newVal = i
        #     if (len(str(i)) - 1) != 0:
        #         i /= 10 * (len(str(i)) - 1)
        #     hash[i] = newVal
        # nums.sort()
        # print(nums)
        # res = ""
        # # for i in nums:
        # #     res+= str(hash[i])
        # return res
