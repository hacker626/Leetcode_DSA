# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        rev1 = self.reverseLL(l1)
        rev2 = self.reverseLL(l2)
        sol = ListNode()
        cur = sol
        carry = 0
        while rev1 or rev2 or carry!=0:
            summ = 0
            if rev1:
                summ += rev1.val
            if rev2:
                summ += rev2.val
            summ += carry
            newNode = ListNode(summ%10)
            carry = summ//10
            cur.next = newNode
            cur = newNode
            rev1 = rev1.next if rev1 else None
            rev2 = rev2.next if rev2 else None
        
        return self.reverseLL(sol.next)  
    def reverseLL(self,head,prev=None):
        if not head:
            return prev
        nxt = head.next
        head.next = prev
        return self.reverseLL(nxt,head)
        
    
        
        s1, s2 = list(), list()
        
        while l1:
            s1.append(l1.val)
            l1 = l1.next
            
        while l2:
            s2.append(l2.val)
            l2 = l2.next
            
        cur = None
        carry = 0
        while s1 or s2 or carry!=0:
            summ = 0
            if s1:
                summ += s1.pop()
            if s2:
                summ += s2.pop()
            summ += carry
            newNode = ListNode(summ%10)
            carry = summ//10
            newNode.next = cur
            cur = newNode
        
        return cur  
            
    