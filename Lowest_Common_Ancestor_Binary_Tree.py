# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root in (None, p, q):
            return root
      
        # Recursively search for p and q in the left subtree
        left_result = self.lowestCommonAncestor(root.left, p, q)
      
        # Recursively search for p and q in the right subtree
        right_result = self.lowestCommonAncestor(root.right, p, q)
      
        # If both left and right subtrees return non-None values,
        # it means p and q are in different subtrees, so current root is the LCA
        if left_result and right_result:
            return root
      
        # If only one subtree contains both nodes (or one node),
        # return the non-None result
        return left_result or right_result
