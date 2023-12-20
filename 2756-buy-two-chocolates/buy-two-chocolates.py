class Solution(object): 

    def smallest(self, prices, s):
        for price in prices:
            if price < s:
                 s = price
        return s
               
    def buyChoco(self, prices, money):

        s1 = 1000
        s2 = 1000

        s1= self.smallest(prices, s1)
        prices.remove(s1)

        s2 =self.smallest(prices, s2)
        prices.remove (s2)

        sum = s1+s2

        if sum <= money:
            return money - sum
        else:
            return money