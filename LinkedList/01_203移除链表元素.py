from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # 创建虚拟头部节点以简化删除过程
        dummy_head = ListNode(next=head)
        
        # 遍历列表并删除值为val的节点
        current = dummy_head
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
            
        return dummy_head.next
    

def build_linked_list(nums):
    dummy = ListNode()
    cur = dummy

    for num in nums:
        cur.next = ListNode(num)
        cur = cur.next
    
    return dummy.next


def print_linked_list(head):
    cur = head

    while cur:
        print(cur.val, end=" -> ")
        cur = cur.next

    print("None")


if __name__ == "__main__":

    nums = [1,2,6,3,4,5,6]
    head = build_linked_list(nums)

    solution = Solution()

    res = solution.removeElements(head, 6)

    print_linked_list(res)