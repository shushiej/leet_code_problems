class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = []
        for i in range(rowIndex + 1):
            val = self.factorial(rowIndex) / (self.factorial(i) * (self.factorial(rowIndex - i)))
            res.append(val)
        return res
            
    def factorial(self, n):
        fact = 1
        for i in range(1,n+1): 
            fact = fact * i
            
        return fact 
        