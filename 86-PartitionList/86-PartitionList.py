# Last updated: 17/07/2026, 15:02:39
class Solution:
    def partition(self, head, x):
        less = ListNode(0)
        greater = ListNode(0)

        less_tail = less
        greater_tail = greater

        current = head

        while current:
            if current.val < x:
                less_tail.next = current
                less_tail = less_tail.next
            else:
                greater_tail.next = current
                greater_tail = greater_tail.next

            current = current.next

        greater_tail.next = None

        less_tail.next = greater.next

        return less.next
        