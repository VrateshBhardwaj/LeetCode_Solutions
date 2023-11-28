class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        index = 0
        i = 0
        ch = ''
        vowel_index = []
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        for ch in s:
            if ch in vowels:
                vowel_index.append(index)
            index += 1
        
        
        string_list = list(s)
        
        for ch in s:
            if ch.lower() in vowels:
                temp = s[vowel_index[-1-i]]
                string_list[vowel_index[i]] = string_list[vowel_index[-1-i]]
                string_list[vowel_index[i]] = temp
                i+=1

        s = ''.join(string_list) 

        return s
        