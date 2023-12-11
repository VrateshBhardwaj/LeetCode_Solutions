class Solution(object):
    def findSpecialInteger(self, arr):
        result = 0
        array_length = len(arr)
        quarter = array_length // 4
        if array_length == 1:
            result = arr[0]
        for i in range(array_length):
            
            last_occurance = float(array_length - arr[::-1].index(arr[i]) - 1)
            difference= ((last_occurance - arr.index(arr[i]))+1)
            

            if difference > quarter:
                result = arr[i]
                break
        return result
        