# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        run = ans
        carry = 0
        while l1 and l2:
            num = l1.val + l2.val + carry

            newNode = ListNode(num % 10)
            run.next = newNode
            run = run.next
            carry = num // 10
            l1 = l1.next
            l2 = l2.next

        if not l1 and l2:
            while not l2:
                num = l2.val


                newNode = List(num+carry)
                run.next = newNode
                run = run.next
                carry = (l2.val + carry) // 10
                l2 = l2.next
        if not l2 and l1:
            while not l1:
                num = l1.val

        while l2:
            num = l2.val + carry

            newNode = ListNode(num % 10)
            run.next = newNode
            run = run.next
            carry = num // 10
            l2 = l2.next
        while l1:
            num = l1.val + carry

            newNode = ListNode(num % 10)
            run.next = newNode
            run = run.next
            carry = num // 10
            l1 = l1.next

        if carry:
            run.next = ListNode(carry)
        
        return ans.next