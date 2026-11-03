# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        p1 = head
        p2 = head
        while n != 0:
            n-=1
            p2 = p2.next
        
        if not p2:
            return head.next
        
        while p2:
            p2 = p2.next
            prev = p1
            p1 = p1.next
        else:
            prev.next = p1.next
        
        return head
        