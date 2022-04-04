class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: [], n: int) -> []:
        first = head
        second = head
        first_ind = 1
        second_ind = 1
        if n == 1 and head.next == None:
            del head
            return 

        while True:
            if abs(first_ind -second_ind) < n: # if the gap is incorrect
                second = second.next
                second_ind += 1
            if second.next == None: # if the gap is correct
                if  n != second_ind: # if second is in the last node 
                    first.next = first.next.next 
                    #print_nodes(head);
                    return head;
                if  n == second_ind: # if second is in the last node 
                    head = head.next 
                    #print_nodes(head);
                    return head
                else:
                    first = fist.next
                    first_ind += 1
                    second = second.next
                    second_ind += 1
            if second.next  != None and abs(second_ind - first_ind) == n:
                second = second.next
                second_ind += 1
                first = first.next
                first_ind += 1


def print_nodes(head):
    node = head
    while node != None:
        print(node.val)
        node = node.next


head                = ListNode(1) 
head.next                = ListNode(2) 
head.next.next = None
 
sl = Solution()
x = sl.removeNthFromEnd(head,1)
#print(x.val)
