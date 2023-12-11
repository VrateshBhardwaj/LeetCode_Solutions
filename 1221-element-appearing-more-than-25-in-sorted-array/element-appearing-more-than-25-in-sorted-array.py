class Solution(object):
    def findSpecialInteger(self, arr):
        array_length = len(arr)
        quarter_length = array_length // 4

        for i in range(array_length - quarter_length):
            if arr[i] == arr[i + quarter_length]:
                return arr[i]