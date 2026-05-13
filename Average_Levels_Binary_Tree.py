from collections import deque

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            level_sum = 0

            for i in range(level_size):
                node = queue.popleft()
                level_sum += node.val          # accumulate sum

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level_sum / float(level_size))   # average = sum / count

        return result
