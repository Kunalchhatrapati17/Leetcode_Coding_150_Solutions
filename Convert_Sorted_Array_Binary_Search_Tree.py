# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        def Build(start , end):
            if start > end:
                return None
            mid = (start+end)//2
            root = TreeNode(nums[mid])
            root.left = Build(start , mid-1)
            root.right = Build(mid+1 , end)

            return root
        return Build(0 , len(nums)-1)
        
        
