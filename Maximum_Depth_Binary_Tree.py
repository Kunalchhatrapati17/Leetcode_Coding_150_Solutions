# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root: #Base Condition if root is Null/Empty
            return 0

        left_depth=self.maxDepth(root.left) #Calculate the left_depth
        right_depth=self.maxDepth(root.right) #Calculate the right_depth

        return 1 + max(left_depth, right_depth) #Return maximum depth
