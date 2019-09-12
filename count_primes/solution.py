# Slow 644ms

class Solution(object):
    def countPrimes(self, n):
        count = 0
        notPrimes = [False] * n
        for i in range(2, n):
            if(notPrimes[i]):
                continue
            count += 1
            for j in range(i*i, n, i):
                notPrimes[j] = True
        return count