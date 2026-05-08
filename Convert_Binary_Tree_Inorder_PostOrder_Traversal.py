# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """

        if not inorder or not postorder:
            return None

        # Last element in postorder is root
        root_val = postorder[-1]
        root = TreeNode(root_val)

        # Find root position in inorder
        mid = inorder.index(root_val)

        # Build left and right subtree
        root.left = self.buildTree(inorder[:mid], postorder[:mid])
        root.right = self.buildTree(inorder[mid + 1:], postorder[mid:-1])

        return root
