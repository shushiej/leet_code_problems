# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        cur = head
        
        while(cur != None):
            nextTemp = cur.next
            cur.next = prev
            prev = cur
            cur = nextTemp
        
        return prev
                
                