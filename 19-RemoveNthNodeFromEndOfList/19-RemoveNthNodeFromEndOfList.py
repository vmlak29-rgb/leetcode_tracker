# Last updated: 17/07/2026, 15:04:12
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head, n):
        # Dummy node helps handle deleting the first node
        dummy = ListNode(0)
        dummy.next = head

        fast = dummy
        slow = dummy

        # Move fast pointer n steps ahead
        for _ in range(n):
            fast = fast.next

        # Move both pointers until fast reaches last node
        while fast.next:
            fast = fast.next
            slow = slow.next

        # Remove nth node from end
        slow.next = slow.next.next

        return dummy.next