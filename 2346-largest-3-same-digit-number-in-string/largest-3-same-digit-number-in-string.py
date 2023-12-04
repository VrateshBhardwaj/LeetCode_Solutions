class Solution(object):
    def largestGoodInteger(self, num):
       
        str = ''
        for i in range(0, len(num)-2, 1):
            if num[i+2] == num[i+1] == num[i]:
                str = 3*num[i]
                break
        #print(str)
        for j in range(0, len(num)-2):
            sbstr = num[j:j+3]

            if str and (str[0] < num[j+2]) and sbstr[0] == sbstr[1] == sbstr[2]:
                str = 3*sbstr[0]
        
        return str 
        