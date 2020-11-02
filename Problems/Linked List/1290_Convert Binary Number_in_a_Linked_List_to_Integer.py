"""
[Solution 1]
Runtime: 28 ms, faster than 79.99% of Python3 online submissions for Convert Binary Number in a Linked List to Integer.
Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Convert Binary Number in a Linked List to Integer.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        binary = ''
        while head:
            binary += str(head.val)
            head = head.next
        return int(binary, 2)

"""
[Solution 2]
Runtime: 24 ms, faster than 93.74% of Python3 online submissions for Convert Binary Number in a Linked List to Integer.
Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Convert Binary Number in a Linked List to Integer.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        res = 0
        while head:
            res = 2 * res + head.val
            head = head.next
        return res

"""
[Solution 3]
Runtime: 28 ms, faster than 79.99% of Python3 online submissions for Convert Binary Number in a Linked List to Integer.
Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Convert Binary Number in a Linked List to Integer.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        res = 0
        while head:
            res = (res << 1) | head.val
            head = head.next
        return res
