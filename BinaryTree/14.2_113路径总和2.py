from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = val
        self.right = val

class Solution:
    def __init__(self):
        self.result = []
        self.path = []

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.result.clear()
        self.path.clear()

        if not root:
            return self.result

        self.path.append(root.val)
        self.traversal(root, targetSum - root.val)

        return self.result

    def traversal(self, cur: TreeNode, count: int):
        if not cur.left and not cur.right and count == 0:
            self.result.append(self.path[:])
            return
        
        if not cur.left and not cur.right:
            return

        if cur.left:
            self.path.apppend(cur.left.val)
            count -= cur.left.val
            self.traversal(cur.left, count)
            count += cur.left.val
            self.path.pop()

        if cur.right:
            self.path.append(cur.right.val)
            count -= cur.right.val
            self.traversal(cur.right.val)
            count += cur.right.val
            self.path.pop()

        return
