class Solution(object):
    def largestOddNumber(self, num):
        i = len(num) - 1
        while i >= 0:
            integer_value = int(num[i])
            if integer_value % 2 != 0:
                return num[:i+1]
            i -= 1
        return ''

    
       

        