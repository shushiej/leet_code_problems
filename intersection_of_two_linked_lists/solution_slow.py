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
        if(headA == None or headB == None):
            return None
        
        ptr1 = headA
        ptr2 = headB
        
        while(ptr1 != None and ptr2 != None):
            if(ptr1 == ptr2):
                return ptr1
            else:
                if(ptr2.next == None):
                    ptr1 = ptr1.next
                    ptr2 = headB
                else:
                    ptr2 = ptr2.next
        return None