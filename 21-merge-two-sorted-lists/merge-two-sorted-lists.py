# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        placeholder = newList = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                newList.next = ListNode(list1.val)
                list1 = list1.next
                newList = newList.next
            else:
                newList.next = ListNode(list2.val)
                list2 = list2.next
                newList = newList.next
        if list1 and not list2:
            while list1:
                newList.next = ListNode(list1.val)
                list1 = list1.next
                newList = newList.next
        if list2 and not list1:
            while list2:
                newList.next = ListNode(list2.val)
                list2 = list2.next
                newList = newList.next
        return placeholder.next



        