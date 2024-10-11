class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        first = set()
        for i in nums:
            if i in first: return True
            first.add(i)
        return False