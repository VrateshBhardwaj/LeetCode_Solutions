class Solution(object):
    def findSpecialInteger(self, arr):

        arrayLength = len(arr)
        quarter = arrayLength // 4
        result = 0
        lastIndex = 0
        firstIndex = 0  
        i = 0
        
        for i, elem in enumerate(arr):

            if elem == arr[firstIndex]:
                lastIndex = i  
            else:
                firstIndex = i  

            difference = lastIndex - firstIndex
            
            if difference  >= quarter:
                result = elem
                break

        return result