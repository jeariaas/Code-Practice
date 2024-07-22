from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        node.next = list1 or list2

        return dummy.next

mergeTwoLists([1,2,4], [1,3,5])

'''
Initialize two nodes, one for storing the head and one that will be updated through but we will be stuck at the end of it.

Run while the two lists arent None,

If one is less than the other, then set the next value of node to be the the node of the list we're currently on.
Move the list to its next node.

Repeat until one list is None

After the loop append the rest of whatever list is not already None. This means we reached the end of one list so we will simply add the rest of the other list to the end

Next we return dummy.next. We return this because dummy points to the first node of node. However the first node of node is also 0 because it is initialized that way.
Therefore we need to return dummy.next because it will point to the actual head of node, which is node.next.
'''