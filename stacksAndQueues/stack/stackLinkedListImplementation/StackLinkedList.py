from arraysAndLinkedLists.linkedList.Node import Node


class StackLinkedList:

    def __init__(self):
        self.head = None
        self.num_elements = 0

    def push(self, element):
        new_node = Node(element)
        if self.num_elements == 0:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.num_elements += 1

    def size(self):
        return self.num_elements

    def is_empty(self):
        if self.num_elements == 0:
            return True
        return False

    def pop(self):
        if self.num_elements == 0:
            return None

        head_node = self.head

        self.head = head_node.next
        head_node.next = None
        self.num_elements -= 1

        return head_node.value
