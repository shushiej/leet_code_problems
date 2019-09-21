# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # Cases where there are vals which replace the 
        # head val ie. [1,1].
        while (head is not None) and (head.val == val):
            head = head.next

        if (head is None):
            return None
        
        cur = head
        while cur.next is not None:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head
                    
            
                