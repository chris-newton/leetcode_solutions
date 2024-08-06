/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    // compare teh two trees with an in-order traversal of both
    
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if ((p == null && q != null) ||
            (p != null && q == null)) {
            return false;
        }
        
        // stopping case
        if (p == null && q == null) {
            return true;
        }
        
        // visit left subtree, then root, then right subtree
        if (!isSameTree(p.left, q.left) || 
            p.val != q.val ||
            !isSameTree(p.right, q.right)) {
            return false;
        }
        
        return true;
    }
}