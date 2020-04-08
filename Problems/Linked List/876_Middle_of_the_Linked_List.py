"""
Runtime: 24 ms, faster than 86.36% of Python3 online submissions for Middle of the Linked List.
Memory Usage: 13.7 MB, less than 7.14% of Python3 online submissions for Middle of the Linked List.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        return slow
