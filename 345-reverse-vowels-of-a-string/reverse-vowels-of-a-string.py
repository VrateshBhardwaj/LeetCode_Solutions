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

        for ch in s:
            if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
                vowel_index.append(index)
                print(index)
            index += 1
        
        vowel_index.reverse()
        string_list = list(s)
        print(string_list)

        for ch in s:
            if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
                temp = s[vowel_index[i]]
                string_list[vowel_index[-1-i]] = string_list[vowel_index[i]]
                string_list[vowel_index[-1-i]] = temp
                i+=1
        s = ''.join(string_list) 

        print(string_list)
        

        return s
        