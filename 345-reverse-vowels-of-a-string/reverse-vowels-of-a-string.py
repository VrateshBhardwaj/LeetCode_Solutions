class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = 'aAeEiIoOuU'
        string_list = list(s)

        left_index = 0
        right_index = len(s) - 1

        while left_index < right_index:

            if string_list[left_index] in vowels and string_list[right_index] in vowels:

                string_list[left_index], string_list[right_index] = string_list[right_index], string_list[left_index]
                left_index += 1
                right_index -= 1
            elif string_list[left_index] not in vowels:
                left_index += 1

            elif string_list[right_index] not in vowels:
                right_index -= 1
                
        return ''.join(string_list) 
        