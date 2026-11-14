# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        
        if head is None or head.next is None:
            return head
        
        prev = head
        node = head.next

        while node is not None:
            nextNode = node.next
            node.next = prev
            prev = node
            node = nextNode
        head.next = None
        return prev
