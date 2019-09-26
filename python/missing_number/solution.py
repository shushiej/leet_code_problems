class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        set_nums = set(nums)
        n = len(nums) + 1
        for num in range(n):
            if num not in set_nums:
                return num
            