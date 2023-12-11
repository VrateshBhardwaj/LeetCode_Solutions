class Solution(object):
    def findSpecialInteger(self, arr):

        arrayLength = len(arr)
        quarter = arrayLength // 4
        result = 0
        for elem in arr:
            firstIndex = float(arr.index(elem)) # finds first index
            lastIndex = arrayLength - arr[::-1].index(elem) - 1 #finds last index
            difference = (lastIndex - firstIndex) 
            
            if difference + 1 > quarter:
                return int(elem)