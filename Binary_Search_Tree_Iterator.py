# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator(object):

    def __init__(self, root):
        
        self.cur = 0
        self.vals = []

        def inorder(node):
            if node:
                inorder(node.left)
                self.vals.append(node.val)
                inorder(node.right)

        inorder(root)

    def next(self):
        """
        :rtype: int
        """
        res = self.vals[self.cur]
        self.cur += 1
        return res

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.cur < len(self.vals)
