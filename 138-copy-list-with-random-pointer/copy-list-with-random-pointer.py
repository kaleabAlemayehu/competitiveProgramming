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
        pairs = {None: None}
        cur = head
        while cur:
            pairs[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            pairs[cur].next = pairs[cur.next]
            pairs[cur].random = pairs[cur.random]
            cur = cur.next

        return pairs[head]