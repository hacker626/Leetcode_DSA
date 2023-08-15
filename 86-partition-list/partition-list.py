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
        temp1,temp2 = ListNode(-1),ListNode(-1)
        prev,post=temp1,temp2

        while(head):
            if(head.val<x):
                prev.next = ListNode(head.val)
                prev=prev.next
            else:
                post.next=ListNode(head.val)
                post=post.next
            head=head.next
        prev.next=temp2.next
        return temp1.next
        