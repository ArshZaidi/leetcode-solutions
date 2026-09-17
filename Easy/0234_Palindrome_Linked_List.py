# Problem: Palindrome Linked List
# Problem ID: 234
# Difficulty: Easy
# Language: Python3
# Runtime: 43 ms
# Memory: 42.1 MB
# Synced From: LeetCode
# Date: 2026-09-17

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Find the middle
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half
        prev = None

        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node

        # Compare both halves
        left = head
        right = prev

        while right:
            if left.val != right.val:
                return False

            left = left.next
            right = right.next

        return True