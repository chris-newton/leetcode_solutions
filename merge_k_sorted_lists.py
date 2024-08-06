# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        newList = curr = ListNode(0)
        q = PriorityQueue()
        
        for l in lists:
            if l:
                q.put((l.val, l))
        while not q.empty():
            val, node = q.get()
            curr.next = ListNode(val)
            curr = curr.next
            node = node.next
            if node:
                q.put((node.val, node))
        return newList.next