import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        s = re.sub('[^a-z0-9]','',s) #replace any character that is not alphanumeric
        
        return s == s[::-1]