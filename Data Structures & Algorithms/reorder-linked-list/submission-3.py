# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        pointer = head
        length = 0
        posToNode = {}
        while pointer is not None:
            length+=1
            posToNode[length] = pointer
            pointer= pointer.next
        print("done")

        midpoint = length//2
        pointer = 1

        dummy = ListNode()
        tail = dummy

        while pointer <= midpoint:
            node = posToNode[pointer] 
            tail.next = node
            tail = tail.next

            node = posToNode[length+1-pointer]
            tail.next = node
            tail = tail.next
            pointer+=1

        if length%2 != 0:
            tail.next = posToNode[midpoint+1]
            tail = tail.next
        tail.next  = None

