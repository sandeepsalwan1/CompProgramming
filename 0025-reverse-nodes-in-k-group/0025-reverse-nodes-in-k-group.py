# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next

# be able to replace the new head
#  1 2 
#  prev is last node
#  21 
# cur is start
#  prev = None
#  cur = head
#  while prev:
#     cur.next = prev
#     prev = cur
# return cur

# iterate through and for each k nodes e.g. for i in range(k):  do above reverse.

# O(n) Tc
# O(1) SC


# 2 4 5
# 1 2 3 4 5

# 2 1 
# 3 0


# 1 k=2

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def get_kth_node(curr: ListNode, k: int) -> ListNode:
            """
            Helper function to get the kth node from current position.
            
            Args:
                curr: Current node
                k: Number of steps to move forward
            
            Returns:
                The kth node if it exists, None otherwise
            """
            while curr and k > 0:
                curr = curr.next
                k -= 1
            return curr
        """
        Reverse nodes of a linked list k at a time.
        
        Args:
            head: Head of the linked list
            k: Group size for reversal
        
        Returns:
            Head of the modified linked list
        """
        # Edge case: empty list or k = 1
        if not head or k == 1:
            return head
        
        # Create a dummy node to simplify edge cases
        dummy = ListNode(0)
        dummy.next = head
        
        # Initialize pointers
        prev_group_end = dummy
        
        while True:
            # Check if there are k nodes remaining
            kth_node = get_kth_node(prev_group_end, k)
            
            # If we don't have k nodes left, we're done
            if not kth_node:
                break
            
            # Save the start of next group
            next_group_start = kth_node.next
            
            # Reverse the current group of k nodes
            prev, curr = kth_node.next, prev_group_end.next
            
            # Reverse k nodes
            for _ in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            # Connect with previous group
            group_start = prev_group_end.next
            prev_group_end.next = kth_node  # kth_node is now the first node
            prev_group_end = group_start    # group_start is now the last node
            
        return dummy.next


    # def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    #     if k == 1: return head

    #     tmp = = ListNode(0,head)
    #     prevEnd = dummy
    #     while True:
    #         kthNode = getKthNode(prevEnd, k)
    #         if not kthNode: return dummy.next
    #         prev, cur = kthNode.next, prevEnd.next
    #         for i in range(k):
    #             temp
    #     return dummy.next
    #     def getKthNode(curr,k):
    #         # cur = head
    #         while curr and k >0:
    #             curr = curr.next
    #             k-=1
    #         return curr