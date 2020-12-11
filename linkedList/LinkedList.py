from Node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out

    def prepend(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node
            return

        node.next = self.head
        self.head = node

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = new_node

    def search(self, value):
        if self.head is None:
            return None

        node = self.head
        if node.value == value:
            return node

        while node.next:
            node = node.next
            if node.value == value:
                return node

        return None

