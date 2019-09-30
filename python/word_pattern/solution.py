class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        dict = {}
        str = str.split()
        
        pattern = [x for x in pattern]
        
        if len(set(pattern)) != len(set(str)) or len(pattern) != len(str): 
            return False
        
        if len(pattern) == len(str):
            for i,char in enumerate(pattern):
                if char in dict:
                    if dict[char] != str[i]: return False           
                dict[char] = str[i]
                
        return True