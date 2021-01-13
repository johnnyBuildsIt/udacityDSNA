class MinBracketReversal:

    @staticmethod
    def minimum_bracket_reversals(input_string):
        if len(input_string) % 2 == 1:
            return -1

        stack = Stack()
        count = 0

        for c in input_string:
            if stack.is_empty():
                stack.push(c)
            else:
                if c == '{':
                    stack.push(c)
                elif c == '}':
                    top = stack.top()
                    if stack.top() == '{':
                        stack.pop()
                    else:
                        stack.push(c)

        while not stack.is_empty():
            pop1 = stack.pop()
            pop2 = stack.pop()
            if pop2 == '}' and pop1 == '{':
                count += 2
            elif pop1 == '}' and pop2 == '}':
                count += 1
            elif pop1 == '{' and pop2 == '{':
                count += 1

        return count


class LinkedListNode:

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self.num_elements = 0
        self.head = None

    def push(self, data):
        new_node = LinkedListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.num_elements += 1

    def pop(self):
        if self.is_empty():
            return None
        temp = self.head.data
        self.head = self.head.next
        self.num_elements -= 1
        return temp

    def top(self):
        if self.head is None:
            return None
        return self.head.data

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0
