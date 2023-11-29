class Solution(object):

    def decimalToBinary (self, n):
        count  = 0
        #string_binary = []

        while n > 0:
            bits = n % 2
            n //= 2
            if bits == 1:
                count += 1
        
        return count

    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        hammingweight = self.decimalToBinary(n)
        return hammingweight

    