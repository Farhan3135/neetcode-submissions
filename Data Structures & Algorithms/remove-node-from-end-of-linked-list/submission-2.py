# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy = ListNode()
        dummy.next = head
        p1 = dummy
        p2 = head
        while n!=0:
            p2 = p2.next
            n-=1
        
        while p2:
            p2 = p2.next
            p1 = p1.next
        else:
            p1.next = p1.next.next
        
        return dummy.next