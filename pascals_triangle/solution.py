class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        
        result = []
        result.append([1])
        for r in range(1, numRows):
            triangle = []
            
            for t in range(0, r + 1):
                val = self.get_factorial(r) / (self.get_factorial(t) * self.get_factorial(r - t))
                triangle.append(val)  
        
            result.append(triangle)
        
        return result
                
    def get_factorial(self, n):
        fact = 1
        for i in range(1,n+1): 
            fact = fact * i
            
        return fact 