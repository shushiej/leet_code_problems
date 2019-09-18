# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if(root == None):
            return None
        
        queue = deque()
        queue.appendleft(root)
        
        while(len(queue) != 0):
            current = queue.popleft()
            temp = current.left
            current.left = current.right
            current.right = temp
            if(current.left != None):
                queue.appendleft(current.left)
            if(current.right != None):
                queue.appendleft(current.right)
        
        return root
                
        
        
        