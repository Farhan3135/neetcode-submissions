# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prev = 0
        dummy = ListNode(0)
        head = dummy
        
        while l1 and l2:
            s = l1.val + l2.val
            s +=prev
            prev = 0
            if s>= 10:
                prev = 1
                s-= 10
            
            newNode = ListNode(s)
            head.next = newNode
            head = head.next
            l1 = l1.next
            l2 = l2.next
        
        if not l1 and not l2:
            if prev == 1:
                newNode = ListNode(1)
                head.next = newNode
            return dummy.next
        
        # figure out ongoing one
        if l1:
            p = l1
        else:
            p=l2

        while p:
            s = p.val + prev
            prev = 0
            if s>= 10:
                prev = 1
                s-= 10
            
            newNode = ListNode(s)
            head.next = newNode
            head = head.next
            p = p.next
        
        if prev ==1:
            newNode = ListNode(1)
            head.next = newNode
            head = head.next

        
        return dummy.next