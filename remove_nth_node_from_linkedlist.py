# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        newHead = ListNode(0)
        newHead.next = head
        fast = slow = newHead
        
        for i in range(n):
            fast = fast.next
            
        while fast.next:
            slow = slow.next
            fast = fast.next
            
        slow.next = slow.next.next
        return newHead.next