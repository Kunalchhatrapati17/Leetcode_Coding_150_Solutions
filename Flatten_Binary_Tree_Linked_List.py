# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        # Process nodes iteratively
        current = root
      
        while current:
            # Check if current node has a left subtree
            if current.left:
                # Find the rightmost node of the left subtree
                # This will be the predecessor of current's right subtree
                predecessor = current.left
                
                while predecessor.right:
                    predecessor = predecessor.right
              
                # Connect the right subtree to the rightmost node of left subtree
                predecessor.right = current.right
              
                # Move the left subtree to the right
                current.right = current.left
              
                # Set left child to None as required for the flattened tree
                current.left = None
          
            # Move to the next node (which is now the right child)
            current = current.right
