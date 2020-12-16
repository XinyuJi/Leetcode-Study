"""
Runtime: 36 ms, faster than 25.00% of Python online submissions for Remove Duplicates from Sorted List.
Memory Usage: 13.6 MB, less than 41.13% of Python online submissions for Remove Duplicates from Sorted List.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        a = head
        while a and a.next:
            if a.val == a.next.val:
                a.next = a.next.next
            else:
                a = a.next
        return head
