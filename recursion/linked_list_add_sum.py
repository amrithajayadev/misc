# https://leetcode.com/problems/add-two-numbers/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add(l1, l2, i, sum1):
    if not l1 and not l2:
        return sum1
    if l1:
        sum1 += pow(10, i) * l1.val
        l1 = l1.next
    if l2:
        sum1 += pow(10, i) * l2.val
        l2 = l2.next
    return add(l1, l2, i + 1, sum1)


def add_opt(l1, l2,carry, l3):
    if not l1 and not l2:
        if carry:
            l3.next = ListNode(carry)
        return
    x = 0
    y = 0
    if l1:
        x = l1.val
        l1 = l1.next
    if l2:
        y = l2.val
        l2 = l2.next
    sum1 = carry + x + y
    carry = sum1//10
    l3.next = ListNode(sum1 % 10)
    return add_opt(l1, l2, carry, l3.next)


def create_linked_list(arr):
    head = None
    curr = None
    for i in arr:
        if not head:
            head = ListNode(i)
            curr = head
        else:
            curr.next = ListNode(i)
            curr = curr.next
    return head


def print_linked_list(head):
    if not head:
        return
    print(head.val, end="->")
    print_linked_list(head.next)

# l1 = create_linked_list([9, 9, 9, 9, 9, 9, 9]) # works
# l2 = create_linked_list([9, 9, 9, 9])

l1 = create_linked_list([2,4,3])
l2 = create_linked_list([5,6,4])
# print_linked_list(l1)

s = add(l1, l2, 0, 0)
print(f"sum={s}")


def return_ll(s):
    head = None
    node = None
    if s == 0:
        return ListNode(s)
    while s > 0:
        if not head:
            head = ListNode(s % 10)
            node = head
        else:
            node.next = ListNode(s % 10)
            node = node.next
        s = s // 10
    return head


final_ll = return_ll(s)
print_linked_list(final_ll)
print("hi")
l3 = ListNode(-1)
add_opt(l1, l2, 0, l3)
print_linked_list(l3.next)
