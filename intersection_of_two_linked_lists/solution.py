# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if(headA == None):
            return None
        
        if(headB == None):
            return None
        
        a,b = headA, headB
        
        while a != b:
            if not a: a = headB
            else: a = a.next
            
            if not b: b = headA
            else: b = b.next
        return a