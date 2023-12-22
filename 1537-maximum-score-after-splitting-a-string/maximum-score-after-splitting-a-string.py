class Solution(object):

    def sum_of_substring_left(self, substring_left):
        sum = 0
        for ch in substring_left:
            if ch == '0':
                sum += 1
        return sum

    def sum_of_substring_right(self, substring_right):
        sum = 0
        for ch in substring_right:
            if ch == '1':
                sum += 1
        return sum

    def maxScore(self, s):

        max = -2**31
        
        for i in range(len(s)):
            substring_left = s[0:i+1:1]
            substring_right = s[i+1:len(s):1]

            if substring_left and substring_right != '':
                sum1 = self.sum_of_substring_left(substring_left)
                sum2 = self.sum_of_substring_right(substring_right)

                if sum1+sum2 > max:
                    max = sum1+sum2
        return max

        