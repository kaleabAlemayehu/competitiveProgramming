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
        prev, curr = None, None
        while n != 0:
            prev = curr
            curr = stack.pop()
            n -= 1
        if len(stack):
            poped = stack.pop()
            poped.next = prev
        else:
            head = head.next

        return head

        