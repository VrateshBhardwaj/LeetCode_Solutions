class Solution(object):
    def kthFactor(self, n, k):
        result = []
        i=1
        res = 0
        for i in range (i,n+1):
            print(i)
            if n%i == 0:
                result.append(i)

        if k>len(result):
            res = -1
            return res
        else:
            res = result[k-1]
            return res

        
        