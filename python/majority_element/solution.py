## 156ms

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums) == 1):
            return nums[0]
        
        seen = {}
        for n in nums:
            if(n not in seen):
                seen[n] = 1
            elif(seen[n] >= len(nums) / 2):
                return n
            else:
                seen[n] += 1