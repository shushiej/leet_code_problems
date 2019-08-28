class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        for c in s:
            num = num * 26 + (ord(c) - ord('A')) + 1
        
        return num