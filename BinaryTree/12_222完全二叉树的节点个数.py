from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        return self.getNodesNum(root)

    def getNodesNum(self, cur):
        if not cur:
            return 0

        leftNum = self.getNodesNum(cur.left)
        rightNum = self.getNodesNum(cur.right)
        treeNum = leftNum + rightNum + 1
        return treeNum
    