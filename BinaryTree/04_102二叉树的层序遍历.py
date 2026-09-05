from typing import List, Optional
import collections 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = collections.deque([root])
        result = []

        while queue:
            level = []
            for _ in range(len(queue)):
                cur = queue.popleft()  # 只要多列不为空，就把当前着一层的节点全部取出来
                level.append(cur.val)
                if cur.left:  # 把这些节点的子节点放进队列
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

            result.append(level)
        return result