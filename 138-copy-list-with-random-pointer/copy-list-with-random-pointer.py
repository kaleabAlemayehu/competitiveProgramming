"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        newList = Node(0) 
        i = head
        j = newList
        hashMap = {}
        while i and i.next:
            j.val = i.val
            hashMap[i] = j
            j.next = Node(0)
            j = j.next
            i = i.next
        if i and j:
            j.val = i.val
            hashMap[i] = j
        i = head
        j = newList
        while i:
            j.random = hashMap.get(i.random, None)
            i = i.next
            j = j.next

        return newList
        
        
            

