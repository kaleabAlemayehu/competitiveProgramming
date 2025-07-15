# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carryOn = 0
        newList = ListNode()
        nl = newList 
        while l1 or l2 or carryOn != 0:
            l1v = l1.val if l1 else 0
            l2v = l2.val if l2 else 0
            s = carryOn + l2v + l1v
            carryOn = s // 10
            s = s % 10
            nl.next = ListNode(s)
            nl = nl.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return newList.next
            

        