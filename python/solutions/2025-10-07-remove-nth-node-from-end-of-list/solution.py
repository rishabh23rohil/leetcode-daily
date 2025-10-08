from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        d = ListNode(0, head)
        l = d
        r = head
        # advance r by n steps
        while n > 0 and r:
            r = r.next
            n -= 1
        # move both until r hits None
        while r:
            l = l.next
            r = r.next
        # remove the target node
        l.next = l.next.next
        return d.next
