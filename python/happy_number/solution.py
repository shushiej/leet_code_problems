class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = {}
        
        while n != 1:
            res = 0
            for i in str(n):
                res += int(i)**2
                
            if res in seen:
                return False
            
            seen[res] = 1
            n = res
            
        if n == 1:
            return True

        
        
        