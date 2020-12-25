from LinkedList import LinkedList


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

    @staticmethod
    def merge(linked_list1, linked_list2):
        if linked_list1 is None:
            return linked_list2
        if linked_list2 is None:
            return linked_list1

        merge_list = LinkedList()
        if linked_list1.head is None and linked_list2.head is None:
            return merge_list

        list1_node = linked_list1.head
        list2_node = linked_list2.head
        while list1_node is not None or list2_node is not None:
            if list1_node is None:
                merge_list.append(list2_node.value)
                list2_node = list2_node.next
            elif list2_node is None:
                merge_list.append(list1_node.value)
                list1_node = list1_node.next
            elif list1_node.value <= list2_node.value:
                merge_list.append(list1_node.value)
                list1_node = list1_node.next
            else:
                merge_list.append(list2_node.value)
                list2_node = list2_node.next
        return merge_list

    @staticmethod
    def flatten(linked_list):
        if linked_list.head is None:
            return linked_list
        return LinkedListHelpers._recursive_flatten(linked_list.head)

    @staticmethod
    def _recursive_flatten(node):
        if node.next is None:
            return LinkedListHelpers.merge(node.value, None)
        return LinkedListHelpers.merge(node.value, LinkedListHelpers._recursive_flatten(node.next))
