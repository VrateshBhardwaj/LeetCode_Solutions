class Solution(object):

    def merge_sort(self, prices):
        
        if len(prices) > 1:
            left_arr = prices[:len(prices)//2]
            right_arr = prices[len(prices)//2:]

            self.merge_sort(left_arr)
            self.merge_sort(right_arr)

            i = 0
            j = 0
            k = 0
            
            while i < len(left_arr) and j < len(right_arr):
                if left_arr[i] < right_arr[j]:
                    prices[k] = left_arr[i]
                    i += 1
                
                else:
                    prices[k] = right_arr[j]
                    j += 1
                
                k += 1
            
            while i < len(left_arr):
                prices[k] = left_arr[i]
                i += 1
                k += 1

            while j < len(right_arr):
                prices[k] = right_arr[j]
                j += 1
                k += 1

        return prices

    def buyChoco(self, prices, money):

        prices = self.merge_sort(prices)

        smallest = prices[0]
        second_smallest = prices[1]

        sum = smallest + second_smallest

        if sum <= money:
            return money - sum
        else:
            return money