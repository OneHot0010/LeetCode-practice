from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy_head = ListNode(0, head)

        # 创建两个指针，慢指针和快指针，并将他们初始化为虚拟节点
        slow, fast = dummy_head, dummy_head

        # 快指针比满指针快 n+1 步
        for i in range(n+1):
            fast = fast.next
        
        # 移动两个指针，直到快速指针达到链表的末尾
        while fast:
            slow = slow.next
            fast = fast.next
        
        # 通过更新第（n-1）个节点的 next 指针删除第 n 个节点
        slow.next = slow.next.next

        return dummy_head.next


'''
初始化后，fast 与 slow 之间的距离保持不变，当 fast 到达 None 时，fast 与 slow 之间的距离也是 n+1。
而待删除节点到 None 的距离是 n，因此待删除节点的前一个节点到 None 的距离正好是 n+1。所以此时 slow 恰好指向待删除节点的前一个节点。
'''