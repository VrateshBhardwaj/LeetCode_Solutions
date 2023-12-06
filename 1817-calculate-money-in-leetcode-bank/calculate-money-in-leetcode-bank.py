class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        initial_week = [1, 2, 3, 4, 5, 6, 7]
        days = 0
        total_money = 0
        week = 0

        for i in range(n):
          week = i // 7
          day = i % 7

          total_money += initial_week[day] + week 

        return total_money
