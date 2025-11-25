class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        # countr = defaultdict(int)
        # for i in nums:
        #     countr[i]+=1
        maxV,maxO = 0,None
        for i,v in count.items():
            if v > maxV:
                maxO = i
                maxV=v
        return maxO
