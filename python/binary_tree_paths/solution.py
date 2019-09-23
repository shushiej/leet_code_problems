# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        paths = []
        
        if root == None:
            return paths
        
        self.dfs(root, "", paths)
        return paths
    
    def dfs(self, root, path, paths):
        path += str(root.val)
        
        if(root.left == None and root.right == None):
            paths.append(path)
            return
        if(root.left != None):
            self.dfs(root.left, path + "->", paths)
        
        if(root.right != None):
            self.dfs(root.right, path + "->", paths)