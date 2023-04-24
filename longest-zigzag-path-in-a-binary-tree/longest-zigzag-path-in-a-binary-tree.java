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
    public int longestZigZag(TreeNode root) {
        if(root==null) {
            return 0;
        }
        return Math.max(moveLeft(root.left,1), moveRight(root.right,1));
    }

    public int moveRight(TreeNode root,int count) {
        if(root==null) {
            return count-1;
        }
        return Math.max(moveLeft(root.left,count+1), moveRight(root.right,1));
    }

    public int moveLeft(TreeNode root, int count) {
        if(root==null) {
            return count-1;
        }
        return Math.max(moveRight(root.right,count+1), moveLeft(root.left,1));
    }
}
