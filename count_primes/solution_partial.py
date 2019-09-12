#Timeout Error
# Attempt at Sieve of Eratosthenes
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        
        
        is_prime = [True] * (n-1)
        p = 2

        while True:
            multiplier = 2
            multiple = p * multiplier

            while multiplier <=n :
                is_prime[multiple - 2]  = False
                multiplier += 1
                multiple = p * multiplier

            for i, prime in enumerate(is_prime):
                if prime and i+2 > p:
                    p = i + 2
                    break
            else:
                break

        count = 0

        for i, prime in enumerate(is_prime):
            if prime:
                count += 1
        return count