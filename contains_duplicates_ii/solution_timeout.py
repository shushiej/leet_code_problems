class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if((nums[i] == nums[j]) & (abs(i - j) <= k) & (i != j)):
                    return True
        return False