# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        return self.checkBalanced(root)['isBalanced']
        
    def checkBalanced(self, root):
        if(root == None):
            return {'isBalanced': True, 'height' : -1}
        
        left_tree = self.checkBalanced(root.left)
        if(not left_tree['isBalanced']):
            return left_tree
        
        right_tree = self.checkBalanced(root.right)
        if(not right_tree['isBalanced']):
            return right_tree
        
        subtree_balanced = abs(left_tree['height'] - right_tree['height']) <= 1
        height = max(left_tree['height'], right_tree['height']) + 1
        
        return {'isBalanced': subtree_balanced, 'height': height}