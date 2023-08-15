# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        temp1 = ListNode(-1)
        temp2 = ListNode(-2)

        prev = temp1
        post = temp2

        while(head):
            if(head.val<x):
                temp = ListNode(head.val)
                prev.next=temp
                prev=prev.next
            else:
                tempo = ListNode(head.val)
                post.next = tempo
                post = post.next
            head=head.next
        prev.next=temp2.next
        return temp1.next
        