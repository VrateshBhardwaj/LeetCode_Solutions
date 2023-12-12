class Solution(object):
    def maxProduct(self, nums):
        largest, second_largest = self.findTwoLargest(nums)
        return (largest - 1) * (second_largest - 1)

    def findTwoLargest(self, nums):
        largest = max(nums[0], nums[1])
        second_largest = min(nums[0], nums[1])

        for num in nums[2:]:
            if num > largest:
                second_largest = largest
                largest = num
            elif num > second_largest:
                second_largest = num

        return largest, second_largest