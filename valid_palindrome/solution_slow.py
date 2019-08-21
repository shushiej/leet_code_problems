import string

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        s = ''.join(c for c in s if c not in set(string.punctuation))
        s = s.replace(" ", "")
        
        return s == s[::-1]