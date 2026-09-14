from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        return self.traversal(root, targetSum - root.val)

    def traversal(self, cur: TreeNode, count: int) -> bool:
        if not cur.left and not cur.right and count == 0:
            return True
        if not cur.left and not cur.right:
            return False

        if cur.left:
            count -= cur.left.val
            if self.traversal(cur.left, count):
                return True
            count += cur.left.val

        if cur.right:
            count -= cur.right.val
            if self.traversal(cur.right, count):
                return True
            count += cur.right.val

        return False


'''
        5
        |
    ——————————
   ｜         ｜
   4          8
   ｜
————————
｜      ｜
1       2

targetSum = 10

从 5 开始

## 第一次递归
第一次调用递归函数，self.traversal(5, 10-5)
左节点为 4，count = 5 - 4 = 1

## 第二次递归
第二次调用递归函数，self.traversal(4, 1)
左节点为 1，count = 1 - 1 = 0

## 第三次递归
第三次调用递归函数，self.traversal(1, 0)
到叶子节点并且count=0，返回 True

## 第三次递归返回 True

## 继续第二次递归
if True:
    return True
返回 True

## 第二次递归返回 True

## 继续第一次递归
if Ture:
    return True
返回 True

## 第一次递归返回 True

递归结束，最终结果为 True
'''


'''
        5
        |
    ——————————
   ｜         ｜
   4          8
   ｜
————————
｜      ｜
2       1

targetSum = 10

从 5 开始

## 第一次递归
第一次调用递归函数，self.traversal(5, 10-5)
左节点为 4，count = 5 - 4 = 1

## 第二次递归
第二次调用递归函数，self.traversal(4, 1)
左节点为 2，count = 1 - 2 = -1

## 第三次递归
第三次调用递归函数，self.traversal(2, -1)
到叶子节点但是 count != 0，返回 False

## 第三次递归返回 False

## 继续第二次递归
if False:
    return True
count = -1 + 2 = 1  # 回到第二次递归，需要将第三次递归减去的值加上，然后继续判断该节点的右节点
右节点为1，此时 count = 1 - 1 = 0

## 进行第四次递归
第四次调用递归函数，self.traversal(1, 0)
到叶子节点且count = 0，返回 True

## 第四次递归返回 True

## 继续第二次递归
if True:
    return True
返回 True

## 第二次递归返回 True

## 继续第一次递归
if Ture:
    return True
返回 True

## 第一次递归返回 True

递归结束，最终结果为 True
'''