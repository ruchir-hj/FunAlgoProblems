# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None



 
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = None
        carry = 0
        sum = 0
        
        while (l1 is not None or l2 is not None or carry):
            if l1:
                a = l1.val
                l1 = l1.next
            else:
                a = 0
            if l2:
                b = l2.val
                l2 = l2.next
            else:
                b = 0
            
            sum = a + b + carry
            carry = sum/10
            res_digit = sum % 10
            
            if (res is None):
                res = ListNode(res_digit)
                res_end = res
            else:
                res_end.next = ListNode(res_digit)
                res_end = res_end.next
        if carry > 0:
            res_end.next = ListNode(carry)
            res_end = res_end.next
        return res
            
        
        
        
