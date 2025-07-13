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
        stack = []
        i =head
        while i:
            stack.append(i)
            i = i.next
        n = len(stack)
        canPop = n // 2
        i = head
        while canPop > 0:
           temp = i.next
           poped = stack.pop() 
           canPop -= 1
           i.next = poped
           poped.next = temp
           i = poped.next
        i.next = None
        
        