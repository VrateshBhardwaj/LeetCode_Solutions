class Solution(object):
    def sum(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        return add(num1, num2)

    def add(self, num1, num2):
        while(num2 != 0):
            carry = num1 & num2
            num1 = num1 ^ num2
            num2 = carry << 1
        return num1