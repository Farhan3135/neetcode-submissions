# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        while fast: 
            if not fast.next or not fast.next.next:
                return False
            
            fast = fast.next.next
            slow = slow.next

            if fast is slow:
                return True
            
        return False