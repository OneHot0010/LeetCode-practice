from typing import List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        def dfs(node):
            if node is None:
                return 

            res.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return res


def build_tree(values):
    if not values:
        return None

    root = TreeNode(values[0])

    queue = deque([root])

    i = 1

    while queue:
        node = queue.popleft()

        # 左节点
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)

        i += 1

        # 右节点
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)

        i += 1

    return root


if __name__ == "__main__":

    root = [1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9]
    values = [1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9]

    root = build_tree(values)