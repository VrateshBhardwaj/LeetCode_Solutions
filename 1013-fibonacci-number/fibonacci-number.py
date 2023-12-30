class Solution(object):

    def fib(self, n):
        return self.helper(n)

    def helper(self, n, memo = {}):
        if n in memo:
            return memo[n]

        if n >= 1 and n <= 2:
            return 1

        if n == 0:
            return 0
        
        memo[n] = self.helper(n-1, memo) + self.helper(n-2, memo)
        return memo[n]

        