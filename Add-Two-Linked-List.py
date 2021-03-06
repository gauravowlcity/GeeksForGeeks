def SumLinkedList(first, second):
    prev = None
    head = ListNode(0)
    temp = None
    carry = 0
    while first and second:
        fdata = 0 if first is None else first.data
        sdata = 0 if second is None else second.data

        sum_ = fdata + sdata + carry

        carry = 1 if sum_ > 10 else 0

        sum_ = sum_ if sum_ < 10 else sum_%10

        temp = Node(sum_)

        if head is None:
            head = temp
        else:
            prev.next = temp

        prev = temp

        if first:
            first = first.next

        if second:
            second = second.next

    if carry > 0:
        temp.next = Node(carry)
    return temp
