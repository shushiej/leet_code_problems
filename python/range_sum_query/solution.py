class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.sum = [0] * (len(self.nums) + 1)

        for ind,_ in enumerate(self.nums):
            self.sum[ind+1] = self.sum[ind] + self.nums[ind]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """        
        return self.sum[j+1] - self.sum[i]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)