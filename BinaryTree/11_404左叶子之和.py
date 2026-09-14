class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:

        # 先判断一个节点是不是空节点，是不是叶子节点
        if root is None:
            return 0

        if root.left is None and root.right is None:  # 通过父结点判断是不是叶子节点
            return 0

        # 如果既不是空节点也不是叶子节点
        leftValue = self.sumOfLeftLeaves(root.left)
        if root.left and not root.left.left and not root.left.right:
            leftValue = root.left.val

        rightValue = self.sumOfLeftLeaves(root.right)

        sum_val = leftValue + rightValue
        return sum_val

    