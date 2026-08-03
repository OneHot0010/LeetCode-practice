class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:
    def __init__(self):
        self.dummy_head = ListNode()
        self.size = 0


    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return

        current = self.dummy_head
        for _ in range(index):
            current = current.next
        
        return current.val
    

    def addAtHead(self, val: int) -> None:
        self.dummy_head.next = ListNode(val, self.dummy_head.next)
        self.size += 1
    
    
    def addAtTail(self, val: int) -> None:
        current = self.dummy_head

        while current.next:
            current = current.next
        current.next = ListNode(val)
        self.size += 1


    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index >= self.size:
            return
        
        current = self.dummy_head
        for _ in range(index):
            current = current.next
        
        current.next = ListNode(val, current.next)
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        current = self.dummy_head
        for _ in range(index):
            current = current.next
        
        current.next = current.next.next

        self.size -= 1


def print_linked_list(linked_list):
    cur = linked_list.dummy_head.next

    while cur:
        print(cur.val, end="->")
        cur = cur.next
    
    print('None')


if __name__ == "__main__":

    
    linked_list = MyLinkedList()

    linked_list.addAtHead(3)
    linked_list.addAtHead(2)
    linked_list.addAtHead(1)

    linked_list.addAtTail(7)

    print(linked_list.get(0))
    print(linked_list.get(1))

    linked_list.addAtIndex(1, 2)

    linked_list.deleteAtIndex(2)

    print_linked_list(linked_list)