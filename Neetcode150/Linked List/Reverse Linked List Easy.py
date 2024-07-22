# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        nNode = None

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
    

    #Solving process
        '''
        While the current head is not Null. ---> This means that the linked list needs to iterate until it reaches the end. 
        At the end, next will be None, then curr will be next meaning that iteration ends it.

        We use three pointers:
        prev = the node before curr
        curr = the node current on
        next = the node after curr

        Step 1:
        We need to save the Node after curr because we need to break the chain between curr and curr.next.
        So we save next to be the node after curr. So next = curr.next

        Step 2:
        We have broken the chain between curr and curr.next, So now we need to make curr.next point to the node behind it. 
        At the start its None, which is what prev is but after it will be a Node. Thus curr.next = prev

        Step 3:
        Curr.next now points to what prev was, but now we need to move prev to what curr currently is. This means we are setting up for the next iteration of the loop
        prev = curr

        Step 4:
        We currently have prev and curr on the same node. But we now need to move curr to what the Node after curr is. However, we had broken the chain from the first node to the second node in step 1.
        But, since we saved the node after curr to the variable next, we can assign curr to be next. curr = next. Thus the chain is restored and prev has the old value of curr and points to null.
        Meaning we have reveresed the first node

        Step 5:
        This will loop until curr is None. This will break the loop and return prev as the head because prev will be the last node before it becomes None.
        return prev.

        '''
  