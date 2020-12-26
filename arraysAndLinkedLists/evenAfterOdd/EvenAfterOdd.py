class EvenAfterOdd:

    @staticmethod
    def arrange_list(linked_list):
        head = linked_list.head
        if head is None or head.next is None:
            return linked_list

        prev = head
        cur = prev.next
        nxt = cur.next
        if head.value % 2 != 0:
            last_odd = head
        else:
            last_odd = None

        while cur is not None:
            if prev.value % 2 == 0 and cur.value % 2 != 0:
                if last_odd is None:
                    head, last_odd = EvenAfterOdd.swap_nodes_last_odd_none(cur, head, last_odd, nxt, prev)
                    if nxt is None:
                        cur = None
                        continue
                    else:
                        cur = nxt
                        nxt = cur.next
                else:
                    last_odd = EvenAfterOdd.swap_nodes(cur, last_odd, nxt, prev)
                    if nxt is None:
                        cur = None
                        continue
                    else:
                        cur = nxt
                        nxt = cur.next
            else:
                if nxt is None:
                    cur = None
                    continue
                else:
                    prev = cur
                    cur = nxt
                    nxt = cur.next
        linked_list.head = head
        return linked_list

    @staticmethod
    def swap_nodes(cur, last_odd, nxt, prev):
        prev.next = nxt
        cur.next = last_odd.next
        last_odd.next = cur
        last_odd = cur
        return last_odd

    @staticmethod
    def swap_nodes_last_odd_none(cur, head, last_odd, nxt, prev):
        prev.next = nxt
        cur.next = head
        head = cur
        last_odd = cur
        return head, last_odd
