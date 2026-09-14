from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # 第一步：如果树为空，递归条件终止
        if not postorder:
            return None

        # 第二步：后序遍历的最后一个节点就是树的根节点
        root_val = postorder[-1]
        root = TreeNode(root_val)

        # 第三步：找切割点
        separator_idx = inorder.index(root_val)

        # 第四步：切割 inorder 数组，得到 inorder 数组的左右半边
        inorder_left = inorder[:separator_idx]
        inorder_right = inorder[separator_idx + 1:]

        # 第五步：切割 postorder 数组，得到 postorder 数组的左右半边
        postorder_left = postorder[:len(inorder_left)]
        postorder_right = postorder[len(inorder_left): len(postorder) - 1]

        # 第六步：递归
        root.left = self.buildTree(inorder_left, postorder_left)
        root.right = self.buildTree(inorder_right, postorder_right)

        # 第七步：返回答案
        return root
    