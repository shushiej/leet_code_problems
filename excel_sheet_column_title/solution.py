class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ""        
        while(n > 0):
            n = n - 1
            toAdd = chr((n % 26) + 65)
            res += toAdd
            n = n / 26
        
        return res[::-1]