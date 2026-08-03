from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(next=head)
        current = dummy_head

        # 必须有 cur 的下一个和下下个才能交换，否则说明已经交换结束了
        while current.next and current.next.next:
            temp = current.next               # 保存待交换的第一个节点
            temp1 = current.next.next.next    # 保存下一轮待处理链表的头节点（第三个节点）

            current.next = current.next.next  # 当前节点指向第二个节点
            current.next.next = temp          # 第二个节点指向第一个节点，完成交换
            temp.next = temp1                 # 第一个节点指向第三个节点，连接后续链表

            current = current.next.next       # current 移动到交换后的第一个节点，为下一轮交换做准备

        return dummy_head.next