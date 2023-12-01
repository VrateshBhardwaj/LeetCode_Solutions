class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        str_word1 = ''
        str_word2 = ''

        for ch in word1:
            str_word1 += ch

        for ch in word2:
            str_word2 += ch
        
        return self.isEqual(str_word2, str_word1)
    
    def isEqual(self, str_word1, str_word2):
        if str_word1 == str_word2:
            return True
        else:
            return False
            
        