class Solution(object):
    def findSpecialInteger(self, arr):
        result = 0
        array_length = len(arr)
        quarter = array_length // 4
        
        for i in range(array_length):
            
            last_occurance = float(array_length - arr[::-1].index(arr[i]) - 1)
            difference= ((last_occurance - arr.index(arr[i]))+1)
            

            if difference > quarter:
                return arr[i]
        