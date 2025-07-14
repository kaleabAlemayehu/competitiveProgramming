# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        N = 0
        i = head
        while i:
            N += 1
            i = i.next
        rmI = N - n
        if rmI == 0:
            return head.next
        l = head
        for i in range(N +1):
            if (i + 1) == rmI:
                l.next = l.next.next
                break
            l = l.next
        return head


        