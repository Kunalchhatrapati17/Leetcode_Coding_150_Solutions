# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype:   
        """
        def dfs(node, current_num):
            if not node:
                return 0

            current_num = current_num * 10 + node.val

            # If leaf node, return the full number
            if not node.left and not node.right:
                return current_num

            # Add left path sum + right path sum
            return dfs(node.left, current_num) + dfs(node.right, current_num)

        return dfs(root, 0)
