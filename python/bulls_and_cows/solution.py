import collections
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        s, g, i = list(secret), list(guess), 0
    	while i < len(s):
    		if g[i] == s[i]:
    			del s[i], g[i]
    			i -= 1
    		i += 1
    	return str(len(secret)-len(s))+'A'+str(sum((collections.Counter(s)&collections.Counter(g)).values()))+'B'