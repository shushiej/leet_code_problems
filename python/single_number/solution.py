class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        freq = {}
        for i in nums:
            try:
                freq.pop(i)
            except:
                freq[i] = 1
        return freq.popitem()[0]