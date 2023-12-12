class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest, second_largest = self.bigNumbers(nums)
        return (largest - 1) * (second_largest - 1)

    def bigNumbers(self, nums):
        largest = max(nums)

        nums.remove(largest)
        
        second_largest = max(nums) 

        return largest, second_largest