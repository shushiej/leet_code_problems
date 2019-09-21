class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if(nums == None or len(nums) == 0):
            return None
        
        # Enter recursive call to build up the tree.
        return self.constructBST(nums, 0, len(nums) - 1)
    
    # Recursive function which creates a new root of the tree based on the left and right pointers.
    def constructBST(self, nums, left, right):
        if(left > right):
            return None
        
        # find the middle element of the list
        mid = left + (right - left) / 2
        
        #initialise the root of the tree/subtree
        current = TreeNode(nums[mid])
        
        #recursively build the left and right nodes of the current node.
        current.left = self.constructBST(nums, left, mid - 1)
        current.right = self.constructBST(nums, mid + 1, right)
        
        return current