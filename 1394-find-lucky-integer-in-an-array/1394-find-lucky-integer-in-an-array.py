class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = Counter(arr)
        maxV=-1
        for i,v in count.items():
            if i==v: maxV=max(maxV,i)
        return maxV