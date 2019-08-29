class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        
        while(n != 0):
            tmp = n / 5
            count = count + tmp
            n = tmp
        
        return count