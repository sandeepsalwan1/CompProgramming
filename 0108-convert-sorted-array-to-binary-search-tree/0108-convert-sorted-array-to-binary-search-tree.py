# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.dummy = ListNode()
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helperSearch(l,r):
            if l > r :
                return None
            m = (l+r)//2 
            root = TreeNode(nums[m])
            root.left = helperSearch(l,m-1)
            root.right  = helperSearch(m+1,r)
            return root
        return helperSearch(0,len(nums) -1 )
    #         while nums: 
    #             if l < r: return None 
    #             l,r = 0, len(nums) - 1
    #             r = m - 1
    #             ListNode(nums[m])
    #             id[input]
    #             return None

    #     if not nums: return TreeNode()
    #     # iterate through and determine what is the total output
    #     for i in nums:
    #         newInput = TreeNode(i)
    #         if i 
    # def addNode(val):
    #     if val < root 

