from DoubleNode import DoubleNode


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        node = DoubleNode(value)

        if self.head is None:
            self.head = node
            self.tail = node
            return

        node.previous = self.tail
        self.tail.next = node
        self.tail = node


