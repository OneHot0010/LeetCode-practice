from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        result = []
        path = []
        if not root:
            return result

        self.traversal(root, path, result)
        return result


    def traversal(self, cur, path, result):
        path.append(cur.val)
        if not cur.left and not cur.right:
            sPath = '->'.join(map(str, path))
            result.append(sPath)
            return
        if cur.left:
            self.traversal(cur.left, path, result) 
            path.pop()  # 回溯
        if cur.right:
            self.traversal(cur.right, path, result)
            path.pop()  # 回溯