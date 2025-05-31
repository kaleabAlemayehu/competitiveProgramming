# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fq = {}
        while head:
            fq[head] = fq.get(head, 0) + 1
            if  fq[head] > 1:
                return True
            head = head.next
        return False

        
