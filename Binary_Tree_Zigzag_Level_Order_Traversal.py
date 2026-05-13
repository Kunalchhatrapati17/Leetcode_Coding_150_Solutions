# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []

        result = []
        queue = deque([root])
        left_to_right = True                      # ← direction flag

        while queue:
            level_size = len(queue)
            current_level = deque()               # ← deque instead of list

            for i in range(level_size):
                node = queue.popleft()

                if left_to_right:
                    current_level.append(node.val)       # ← add to RIGHT end
                else:
                    current_level.appendleft(node.val)   # ← add to LEFT end

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(list(current_level))    # ← convert deque to list
            left_to_right = not left_to_right     # ← flip direction

        return result  
