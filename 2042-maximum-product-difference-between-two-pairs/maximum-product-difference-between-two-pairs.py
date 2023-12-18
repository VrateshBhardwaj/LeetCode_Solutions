class Solution(object):
    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum = -2147483648

        for num in nums:
            if num > maximum:
                maximum = num
        nums.remove(maximum)

        second_maximum = -2147483648
        for num in nums:
            if num > second_maximum:  
                second_maximum = num
        nums.remove(second_maximum)

        minimum = 2147483647
        for num in nums:
            if num < minimum:
                minimum = num
        nums.remove(minimum)

        second_minimum = 2147483647
        for num in nums:
            if num < second_minimum:  
                second_minimum = num
        nums.remove(second_minimum)

        return (maximum * second_maximum) - (second_minimum * minimum)
