from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 1:
            return TreeNode(nums[0])

        node = TreeNode(0)
        # 找到数组中最大的值和对应的下表
        maxValue = 0
        maxValueIndex = 0

        for i in range(len(nums)):
            if nums[i] > maxValue:
                maxValue = nums[i]
                maxValueIndex = i
        node.val = maxValue

        # 最大值所在的下标左区间，构造左子树
        if maxValueIndex > 0:  # 判断maxValueIndex > 0，因为要保证左区间至少有一个数值。
            new_list = nums[:maxValueIndex]
            node.left = self.constructMaximumBinaryTree(new_list)
        # 最大值所在的下标右区间，构造右子树
        if maxValueIndex < len(nums) - 1:  # maxValueIndex < (nums.size() - 1)，确保右区间至少有一个数值。
            new_list = nums[maxValueIndex+1:]
            node.right = self.constructMaximumBinaryTree(new_list)
        return node
