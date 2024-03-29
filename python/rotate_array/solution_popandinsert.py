# 168ms

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if k < 0:
            return None
        
        for _ in range(k):
            nums.insert(0, nums.pop())