class TreeNode:
    def __init__(self, val: int=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode):
        return self.getdepth(root)

    def getdepth(self, node):
        if not node:
            return 0

        leftheight = self.getdepth(node.left)
        rightheight = self.getdepth(node.right)
        height = 1 + max(leftheight, rightheight)
        return height