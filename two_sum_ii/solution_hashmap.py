class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}

        for i,n in enumerate(numbers):
            total = target - n

            if total not in seen:
                seen[n] = i + 1
            else:
                return [seen[total], i + 1]