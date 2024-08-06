# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        A = B = head
        
        # move A to kth node from beginning
        for i in range(k-1):
            A = A.next
        
        # store kth node
        kthNode = A
        A = A.next
        
        # move B to kth node from end
        while A:
            A = A.next
            B = B.next
        
        # swap kthNode and B's values
        kthNode.val, B.val = B.val, kthNode.val
        return head