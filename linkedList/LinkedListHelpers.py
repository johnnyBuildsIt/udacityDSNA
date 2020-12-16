class LinkedListHelpers:

    @staticmethod
    def is_circular(linked_list):
        slow_runner = linked_list.head
        fast_runner = linked_list.head

        while slow_runner is not None and fast_runner is not None:
            slow_runner = slow_runner.next
            if fast_runner.next is None:
                fast_runner = None
            else:
                fast_runner = fast_runner.next.next
            if fast_runner == slow_runner and fast_runner is not None and slow_runner is not None:
                return True
        return False
