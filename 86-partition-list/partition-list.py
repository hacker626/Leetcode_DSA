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
        if(head == None):
            return head
        temp = []
        temp2 = []
        temp3 = []


        while(head):
            if(head.val>=x):
                break
            temp.append(head.val)
            head=head.next
        
        while(head):
            if(head.val>=x):
                temp2.append(head.val)
            else:
                temp3.append(head.val)
            head=head.next
        finalAns = temp+temp3+temp2

        tempNode=ListNode(-1)
        headNode = ListNode(finalAns[0])
        tempNode.next = headNode

        for i in range(1,len(finalAns)):
            tempo = ListNode(finalAns[i])
            headNode.next=tempo
            headNode=headNode.next
        return tempNode.next


        # temp = ListNode(-1)
        # temp.next = head
        # prev = temp
        # while(head):
        #     if(head.data>=x):
        #         break
        #     prev=head
        #     head=head.next
        # temp2 = ListNode(-2)
        # temp2.next=head

        # while(head):
        #     if(head.data<x):
        #         prev.next=head
        #         prev=prev.next

            
        