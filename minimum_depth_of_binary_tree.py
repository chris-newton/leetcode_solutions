# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        if root == None:
            return 0
        elif root.left == None or root.right == None:
            return 1 + self.minDepth(root.right) + self.minDepth(root.left)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))