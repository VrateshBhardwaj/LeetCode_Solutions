class Solution(object):
    
    def minOperations(self, s):

        n = len(s)
        changes = 0

        if n == 1:
            return 0

        for i in range(n):

            if i % 2 == 0 and s[i] == '1':
                changes += 1

            if i % 2 == 1 and s[i] == '0':
                changes += 1

        return min(changes, n - changes)

        