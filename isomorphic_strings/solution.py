class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapping = {}
        for cs, ct in zip(s, t):
            try:
                if mapping[cs] != ct:
                    return False
            except:
                if ct in mapping.values():
                    return False
                mapping[cs] = ct
        return True