#Timeout Error

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        
        
        prime  = [True for i in range(n + 1)]
        
        p = 2
        while(p * p <=n):
            if(prime[p] == True):
                for i in range(p * 2, n + 1, p):
                    prime[i] = False
            p += 1
            
        prime[0] = False
        prime[1] = False
        count = 0
        for p in range(n + 1):
            if prime[p]:
                count += 1
        return count