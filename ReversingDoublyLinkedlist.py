    if not head.next:
        return head

    else:
        current = head
        while current:
            nxt = current.next
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = nxt
        head = temp.prev
        return head
