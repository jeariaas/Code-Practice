class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        nextNode = head.next
        print(nextNode.val)
        

input_list = [0,1,2,3,4]
nodes = [ListNode(val = i) for i in input_list]
for i in range(len(nodes)-1):
    nodes[i].next_ele = nodes[i+1]
s = Solution()
s.reverseList(nodes[0])
  