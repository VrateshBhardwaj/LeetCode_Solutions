# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        list = []
        self.inorderHelper(root, list)
        return list
        
    def inorderHelper(self, root, list):
         if root:
            self.inorderHelper(root.left, list)
            list.append(root.val)
            self.inorderHelper(root.right, list)

