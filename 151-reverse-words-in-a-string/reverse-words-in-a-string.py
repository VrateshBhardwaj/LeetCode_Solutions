class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        str = s.strip()
        print(str)
        res = str.split()
        op = res[::-1]
        print(op)
        
        result = ' '.join(op)
        return result
            
            
        