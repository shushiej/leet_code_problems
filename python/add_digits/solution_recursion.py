class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if(len(str(num)) == 1):
            return num
        
        digits = [int(x) for x in str(num)]
        tot = sum(digits)
        
        return self.addDigits(tot)