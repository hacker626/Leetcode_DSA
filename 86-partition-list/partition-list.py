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
        temp1,temp2=[],[]
        while(head):
            if(head.val<x):
                temp1.append(head.val)
            else:
                temp2.append(head.val)
            head=head.next
        ans = ListNode(-1)
        temp = ans
        for i in temp1+temp2:
            temp.next=ListNode(i)
            temp=temp.next
        return ans.next