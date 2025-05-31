# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = head 
        if head:
            f = head.next
        else:
            return False
        while s != f:
            if f and f.next:
                f = f.next.next
                s = s.next
            else:
                return False
        return True

        
