class MyLinkedList:
    class Node:
        def __init__(self, value):
            self.val = value
            self.next = None

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        if self.head is None:
            return -1
        else:
            n = 0
            node1 = self.head
            while n < index and node1:
                n += 1
                node1 = node1.next
            if node1:
                return node1.val
            else:
                return -1

    def addAtHead(self, val: int) -> None:
        new_node = self.Node(val)
        new_node.next = self.head
        self.head = new_node

    def addAtTail(self, val: int) -> None:
        new_node = self.Node(val)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        else:
            n = 0
            node1 = self.head
            while n < index - 1 and node1:
                n += 1
                node1 = node1.next
            if node1:
                new_node = self.Node(val)
                new_node.next = node1.next
                node1.next = new_node

    def deleteAtIndex(self, index: int) -> None:

        if index == 0:
            self.head = self.head.next
        else:
            n = 0
            node1 = self.head
            while n < index - 1 and node1:
                n += 1
                node1 = node1.next
            if node1 and node1.next:
                node1.next = node1.next.next
