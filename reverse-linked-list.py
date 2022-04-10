# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: []) -> []:
        curr    = head # 2
        prev    = None
        _next    = None
        


        while curr != None:

            _next = curr.next
            curr.next = prev
            prev = curr
            curr = _next

        head = prev
        print_nodes(head)


        


def print_nodes(head): 
    x = head
    while x != None:
        print(x.val)
        x = x.next


head =  ListNode(1)
head.next =  ListNode(2)
head.next.next =  ListNode(3)
head.next.next.next = None 
ts = Solution()
ts.reverseList(head)
