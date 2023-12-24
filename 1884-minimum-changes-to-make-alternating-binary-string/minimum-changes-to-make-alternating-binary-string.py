class Solution(object):

    def minOperations(self, s):

        n = len(s)
        changes1 = 0
        changes2 = 0

        str1 = ''
        str2 = ''

        for i in range(0, n):
            if (i % 2 == 0):
                str1 += '0'
            if(i % 2 != 0):
                str1 +='1'

        for i in range(0, n):
            if (i % 2 == 0):
                str2 += '1'
            if(i % 2 != 0):
                str2 += '0'
        
        for i, ch in enumerate(s):
            if ch != str1[i]:
                changes1 += 1
            if ch != str2[i]:
                changes2 += 1

        print(str1, str2)
        return min(changes1, changes2)


        