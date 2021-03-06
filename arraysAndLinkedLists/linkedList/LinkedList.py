from .Node import Node


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

    def remove(self, value):
        if self.head is None:
            return

        if self.head.value == value:
            removed_node = self.head
            self.head = removed_node.next
            removed_node.next = None
            return
        elif self.head.next is None:
            return

        node = self.head
        while node.next:
            node = node.next
            if node.next:
                next_node = node.next
                if next_node.value == value:
                    node.next = next_node.next
                    next_node.next = None
                    return
            else:
                return

    def pop(self):
        if self.head is None:
            return None

        node = self.head
        self.head = node.next
        node.next = None

        return node.value

    def insert(self, value, position):
        if self.head is None or position == 0:
            self.prepend(value)
            return

        node = self.head
        for i in range(1, position):
            if node.next is None:
                self.append(value)
                return
            node = node.next

        new_node = Node(value)
        new_node.next = node.next
        node.next = new_node

    def size(self):
        if self.head is None:
            return 0

        node = self.head
        count = 1
        while node.next is not None:
            count += 1
            node = node.next

        return count

    def reverse(self):
        if self.head is None or self.head.next is None:
            return self.to_list()

        cur_node = self.head
        next_node = cur_node.next
        prev_node = None

        while cur_node:
            cur_node.next = prev_node
            if next_node is None:
                self.head = cur_node
                return
            prev_node = cur_node
            cur_node = next_node
            next_node = cur_node.next
