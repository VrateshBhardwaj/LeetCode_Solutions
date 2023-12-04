class Solution(object):
    def largestGoodInteger(self, num):
       
        str = ''
        for i in range(0, len(num)-2):
            if num[i+2] == num[i+1] == num[i]:
                str = 3*num[i]
                break
            else:
                str = ''
        
        if str:
            for j in range(0, len(num)-2):
                 if (str[0] < num[j+2]) and num[j+2] == num[j+1] == num[j]:
                    str = 3*num[j]
        

        return str 