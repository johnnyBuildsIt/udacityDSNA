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
                prev.next = nxt
                if last_odd is None:
                    cur.next = head
                    head = cur
                    last_odd = cur
                    if nxt is None:
                        cur = None
                        continue
                    else:
                        cur = nxt
                        nxt = cur.next
                else:
                    cur.next = last_odd.next
                    last_odd.next = cur
                    last_odd = cur
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
            # if (prev.value % 2 == 0 and cur.value % 2 == 0) or \
            #         (prev.value % 2 != 0 and cur.value % 2 != 0) or \
            #         (prev.value % 2 != 0 and cur.value % 2 == 0):
            #     prev = cur
            #     cur = nxt
            #     if cur is not None:
            #         nxt = cur.next
            # elif prev.value % 2 == 0 and cur.value % 2 != 0:
            #     prev.next = nxt
            #     if last_odd is None:
            #         cur.next = head
            #         head = cur
            #         last_odd = head
            #         cur = nxt
            #         nxt = cur.next
            #     else:
            #         cur.next = last_odd.next
            #         last_odd.next = cur
            #         last_odd = cur
            #         if nxt is not None:
            #             #prev = cur
            #             cur = nxt
            #             nxt = cur.next
            #         else:
            #             cur = None
        linked_list.head = head
        return linked_list
