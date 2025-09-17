class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [10**10] * len(nums1)
        for v,i in enumerate(nums1):
            cur = float('-inf')
            for idx,j in enumerate(nums2):
                if j ==i:
                    cur= j
                    continue
                if cur != float('-inf'):
                    if j > cur:
                        res[v] = j
                        break
            
            if res[v]== 10**10: 
                res[v]=-1
        return res
