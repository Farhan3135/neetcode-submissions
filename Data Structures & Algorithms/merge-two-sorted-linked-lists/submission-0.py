# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        if not list1:
            return list2
        elif not list2:
            return list1
        
        if list1.val<= list2.val:
            head = list1
            minNode = list1
            maxNode = list2
        else:
            head = list2
            minNode = list2
            maxNode = list1
        
        while minNode and maxNode: 
            if minNode.val <= maxNode.val:
                pass
            else:
                holder = minNode
                minNode = maxNode
                maxNode = holder
            
            while not minNode.next is None and minNode.next.val <= maxNode.val:
                minNode = minNode.next
            else:
                nextNode = minNode.next
                minNode.next = maxNode
                minNode = nextNode
        return head