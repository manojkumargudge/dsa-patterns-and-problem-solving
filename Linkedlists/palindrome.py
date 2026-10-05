'''Given the head of a singly linked list, return true if it is a palindrome or false otherwise.'''

#Find middle → reverse second half → compare both halves.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def ispalindrom(self,head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if fast:
            slow = slow.next

        prev = None

        while slow:
            temp = slow.next
            slow.next = prev 
            prev = slow
            slow = temp

        left = head
        right = prev

        while right:
            if left.val != right.val:
                return False

            left = left.next
            right = right.next

        return True

