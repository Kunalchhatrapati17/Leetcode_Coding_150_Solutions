class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        #1. Base Condition to check if root is Null
        if not root:
          return False

        #2. Check if there is a leaf node 
        # If not compare the values root.val==targetSum
        if not root.left and not root.right:
               return root.val==targetSum

        #Recurse down the tree, from left to right to find the valid path
        remaining_sum=targetSum-root.val # Calculate the remaining_sum
        return self.hasPathSum(root.left, remaining_sum)  or self.hasPathSum(root.right, remaining_sum)
