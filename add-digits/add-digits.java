class Solution {
    public int addDigits(int num) {
        int res;
         res = num;
        while(res>=10)
        {
           int addition = 0;
           while(res>0)
           {
               addition=addition+res%10;
               res=res/10;
           }
           res =addition;
        }
        return res;
    }
}