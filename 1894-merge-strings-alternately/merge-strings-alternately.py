class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = ""
        len_word_1 = len(word1)
        len_word_2 = len(word2)
        i=0
        j=0

        while(i<len_word_1) and (j<len_word_2):
            result += word1[i]
            result += word2[j]

            i += 1
            j += 1

        while i < len_word_1:
            result += word1[i]
            i += 1
        
        while j < len_word_2:
            result += word2[j]
            j += 1

        return result
            
        