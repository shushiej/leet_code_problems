# 44ms

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if k == 0:
            return None
        
        k %= len(nums)
        nums[k:], nums[:k] = nums[:-k], nums[-k:]
