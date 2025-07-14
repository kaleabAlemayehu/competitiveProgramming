# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        stack = []
        i = head
        while i:
            stack.append(i)
            i = i.next
        removeIndex = len(stack) - n
        if removeIndex == 0:
            return head.next
            
        stack[removeIndex - 1].next =  stack[removeIndex].next
        return head


        