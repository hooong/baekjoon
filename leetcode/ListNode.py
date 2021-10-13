class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def make_list_node(values):
    tmp = None
    for v in values[::-1]:
        tmp = ListNode(val=v, next=tmp)

    return tmp


def print_list_node(nodes):
    values = []
    tmp = nodes
    while tmp:
        values.append(tmp.val)
        tmp = tmp.next

    return values
