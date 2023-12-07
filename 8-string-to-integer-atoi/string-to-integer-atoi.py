class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        i, sign, result = 0, 1, 0

        while i < len(s) and s[i].isspace():
            i += 1

        if i < len(s) and (s[i] == '-' or s[i] == '+'):
            sign = -1 if s[i] == '-' else 1
            i += 1

        
        while i < len(s) and s[i].isdigit():

            digit = int(s[i])

            if result > (2**31 - 1) // 10 or (result == (2**31 - 1) // 10 and digit > 7):
                return -2147483648 if sign == -1 else 2147483647

            result = result * 10 + digit
            i += 1

        return sign * result

