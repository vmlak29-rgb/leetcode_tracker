# Last updated: 17/07/2026, 15:03:13
class Solution:
    def rotateRight(self, head, k):

        # Empty list or single node
        if not head or not head.next:
            return head

        # Find length and last node
        length = 1
        tail = head

        while tail.next:
            tail = tail.next
            length += 1

        # Reduce unnecessary rotations
        k = k % length

        if k == 0:
            return head

        # Make circular list
        tail.next = head

        # Find new tail
        steps = length - k

        new_tail = tail

        while steps:
            new_tail = new_tail.next
            steps -= 1

        # New head is after new tail
        new_head = new_tail.next

        # Break the circle
        new_tail.next = None

        return new_head
        