
'''
0 1 2 3 4 5
'''

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def middle_of_linked_list(head: Node) -> int:
    slow = head
    fast = head

    while fast:
        print(slow.val, fast.val)
        if fast.next is not None:
            fast = fast.next
            print(fast.val)
            if fast.next is not None:
                fast = fast.next
                print(fast.val)
                slow = slow.next
                continue
            return slow.next.val
        return slow.val

def build_list(nodes, f):
    val = next(nodes, None)
    if val is None: return None
    nxt = build_list(nodes, f)
    return Node(f(val), nxt)

if __name__ == '__main__':
    head = build_list(iter(input().split()), int)
    res = middle_of_linked_list(head)
    print(res)
