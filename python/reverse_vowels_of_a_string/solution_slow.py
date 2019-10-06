# Timeout

def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ["a","e","i","o","u", "A", "E", "I", "O", "U"]
        
        vow = [str(v) for v in s if v in vowels]
        idx = [i for i,_ in enumerate(s) if _ in vowels]
        
        vow.reverse()
        dic = dict(zip(idx,vow))
        
        for k,v in dic.items():
            x = list(s)
            x[k] = v
            s = "".join(x)
        
        return s
        
        
                