# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        
        #Base Condition
        if not preorder or not inorder:
            return None

        root=TreeNode(preorder[0]) #Calculate the root
        mid=inorder.index(preorder[0]) # Calculate middle element

        root.left=self.buildTree(preorder[1:mid+1], inorder[:mid]) #Left SubTree
        root.right=self.buildTree(preorder[mid+1:], inorder[mid+1:]) #Right SubTree

        return root #Returns the Root Node
