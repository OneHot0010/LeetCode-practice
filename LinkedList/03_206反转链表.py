from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode):
        cur = head
        pre = None

        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp

        return pre
    

def build_linked_list(nums):

    dummy_head = ListNode()

    current = dummy_head
    for num in nums:
        current.next = ListNode(num)
        current = current.next
    
    return dummy_head.next


def print_linked_list(head):

    cur = head
    while cur:
        print(cur.val, end='->')
        cur = cur.next

    print('None')


if __name__ == "__main__":

    nums = [1, 2, 3]

    head = build_linked_list(nums)

    solution = Solution()

    res = solution.reverseList(head)
    print_linked_list(res)