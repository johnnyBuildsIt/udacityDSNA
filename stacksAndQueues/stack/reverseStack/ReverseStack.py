from stacksAndQueues.stack.stackLinkedListImplementation.StackLinkedList import StackLinkedList


class ReverseStack:

    @staticmethod
    def reverse(stack):
        new_stack = StackLinkedList()

        while not stack.is_empty():
            new_stack.push(stack.pop())
        return new_stack
