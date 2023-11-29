class Solution(object):

    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count  = 0

        while n > 0:
            bits = n % 2
            n //= 2
            if bits == 1:
                count += 1
        
        return count

    