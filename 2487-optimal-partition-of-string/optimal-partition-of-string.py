class Solution(object):
    def partitionString(self, s):
        str=""
        count = 0
        for i in s:
            if i in str:
                str=''
                count = count+1
                #print(str)

            str = str+i
            

        if len(str)!=0:
            count = count+1
            
        return count