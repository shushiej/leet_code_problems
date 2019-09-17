# 72ms

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        positions = {}
        for idx, num in enumerate(nums):
            if num in positions and (idx - positions[num] <= k):
                return True
            positions[num] = idx
        return False